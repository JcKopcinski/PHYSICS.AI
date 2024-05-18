import csv

class ConstraintWarning:
    def __init__(self,knowns,objects,object_num,new_known_var_name):
        self.knowns = knowns
        self.objects = objects
        self.object_name = objects[object_num]
        self.object_num = object_num
        self.new_known_var_name = new_known_var_name
        
        self.warnings = []
        self.generate_warning_messages()


    def generate_warning_messages(self):
        with open('warnings.csv') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            header = next(lines)
            for i,line in enumerate(lines):
                self.warnings.append({"id": i,"new_known": line[0],"past_known": line[1], "msg": line[2]})

  
    def consolodate_by_seq(self,select):
        seq_nums = set([sel['seq_num'] for sel in select])

        c = []
        for i,seq_num in enumerate(seq_nums):
            group = [f"{sel['warning']} ({sel['msg']}) and " for sel in select if sel['seq_num'] == seq_num]
            c.append({"choice": i+1,"seq_num": seq_num,"msg": group})
        return c

    def print_warning(self,msg):
        print(msg.replace("the object",f"the {self.object_name}"))

    #look for a warning about a newly claimed known variable
    def warning_needed(self):
        print()
        print(f"O.K., you are claiming to  know {self.new_known_var_name} for the {self.object_name}.")

        #find all warnings that have to do with the new variable the student is claiming to know
        possible_warnings = [warning for warning in self.warnings if warning['new_known'] == self.new_known_var_name]

        #now pull all knowns that have to do with a past known and claimed new known in the possible_warnings
        past_knowns = [
                            {
                                "warning_id": warning['id'],
                                "warning": warning['msg'],
                                "response": known['response'],
                                "seq_num": known['seq_num'],
                                "var_name": known['var_name'],
                                "new_known": warning['new_known']
                            }
                            for warning in possible_warnings for known in self.knowns 
                                if 
                                known['object_num'] == self.object_num and 
                                known['var_name'] == warning["past_known"] and
                                warning['new_known'] == self.new_known_var_name  
                    ]
        #https://stackoverflow.com/questions/11092511/list-of-unique-dictionaries
        #called "dict comprehension"
        past_knowns = list({v['warning_id']:v for v in past_knowns}.values())
      
        if past_knowns:
            #make the menu of choices
            select = [
                        {
                            "choice": i+1,
                            "msg": f"which you said was {known['var_name']} = {known['response']}",
                            "variable": known['var_name'],
                            "seq_num": known['seq_num'],
                            "warning": known['warning']
                        } 
                        for i,known in enumerate(past_knowns)
                    ]

            #consolidate by seq_num
            csel = self.consolodate_by_seq(select)

            #only one past known is found
            if len(csel) == 1:
                print("But be sure that: ")
                for msg in csel[0]['msg']:
                    self.print_warning(msg)
                seq = input(f"Is this the right scenario for the {self.new_known_var_name} you now claim to know? [y/n]: ")
                if seq.lower() == 'n':
                    seq = input("Ok, will it fit somewhere else in the problem then? [y/n]: ")
                    if seq.lower() == 'n':
                        return {"action": "reject"}
                    return {"action": "keep_seq"}
                return {"action": "seq_num","seq_num": select[0]['seq_num']}

            #more than one past known. Compile scenario and present a menu
            elif len(csel) > 1:
                print("But be sure that: ")
                for sel in csel:
                    print(f"Scenario {sel['choice']}: ")
                    for msg in sel['msg']:
                        self.print_warning(msg)
                seq = input(f"Which is the right scenario that goes with  {self.new_known_var_name} that you now claim to know? (Select 1..{len(select)} or n for none): ")
                
                #they chose a senario. Return the seq_num to override one from binary string
                if isnumeric(seq):
                    seq = int(seq) - 1
                return {"action": "seq_num","seq_num": select[seq]['seq_num']}

                #Not a number means no scenario matches. Possibly they are observing a new variable 
                #from another part of the problem. 
                if seq.lower() == 'n':
                    seq = input("Ok, will it fit somewhere else in the problem then? [y/n]: ")

                    #confusion. They may not actually know what they thought
                    if seq.lower() == 'n':
                        return {"action": "reject"}

                    #ok, they insist, so log it, but keep the seq_num pulled from the binary string.
                    return {"action": "keep_seq"}
                
        # no past knowledge at all. Just accept what they claim to see
        return {"action": "take_it"}
