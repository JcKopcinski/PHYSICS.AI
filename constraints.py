# untested pseudo-code for handling
# constraints in the equations

# Assume knows are collected in some
# kind of Python list (of dictionaries)

# example

#created dynamically as a response to "do you see an object in the problem?" questions
objects = {3: "stone", 5: "truck", 1: "window"}

#creates dynamically as a response to "do you know XXX about object YYY?" questions
knowns = [
            {"object": 3, "equation": 2, "variable": 1, "response": "the speed of the stone after it accelerated"},
            {"object": 5, "equation": 1, "variable": 2, "response": "it says the the truck is initally at x=0"}
]

contraints = [
    {
        "if_yes_equ": 1, "if_yes_var": 1,
        "warn_if_known_equ": 1, "warn_if_known_var": 5,
        "message": f"x is the position of the {get_object_in_question()} at the end of the time interval you said you knew was {get_response_for(object,1,1)}" 
    },
]


#see if equation and variable is known about object
def is_known(object,equation,variable):
    for known in knowns:
        if known['object'] == object and known['equation'] == equation and known['variable'] == variable:
            return True
    return False

#get whaat the student said about knowning equation and variable for object
def get_response_for(object,equation,variable):
    for known in knowns:
        if known['object'] == object and known['equation'] == equation and known['variable'] == variable:
            return known['response']
    return "??Unknown??"


#returns false if student is not understanding
#variale constraints
def warning(object,equation,variable):
    for constraint in constraints:
        if (    constraint['if_yes_equ'] == equation and 
                constraint['if_yes_var'] == variable and 
                is_known(object,constraint['warn_if_known_eqn'],contraint['warn_if_known_var'])):
                    print(contraint['message'])
                    response = input("yes or no?")
                    return(response == "no")

    #ok to accept yes as answer to question that triggered the constrains
    return(true)

