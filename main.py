import sympy as sp
from function_definitions import *

NUM_BITS = 36 #number of bits in bitString. (current implementation NUM_BITS must be a divisible integer of ATTRIBUTES)

if __name__ == "__main__":

    bitString = generate_random_string(NUM_BITS)
    bitList = split_bitstring(bitString)

    vals = [int(i, 2) for i in bitList] #convert bitStrings to integers

    objectList = [] #initialize object list to empty
    knownObjects = []
    #-------------------------DEBUG------------------
    print("bitString: " + bitString)
    print(bitList)
    print(vals)
    #-------------------------DEBUG------------------

    #count by 3 on each iteration
    for i in range(0, len(vals), 4):
        objectNumber = vals[i] #the object
        equationNumber = vals[i+1] #the equation
        variableNumber = vals[i+2] #the variable
        sequenceNumber = vals[i+3] #the sequence

        #check if the object already exists
        objectExists = False
        if knownObjects:
            for item in knownObjects:
                if objectNumber == item["objectNumber"]:
                    object_name = item["object_name"] #set the object's name
                    objectExists = True #object already exists
                    print("here")

        if objectList: #check if object list is empty
            if not objectExists: #check if object has already been encountered
                object_response = input("Do you see any more objects in the problem? ")
                if(object_response == 'y' or object_response == "yes"): #check if response is affirmative
                    object_name = input("What is the object? ") #get the object's name
                else:
                    print("No more objects seen...skipping")
                    break
        else:
            object_response = input("Do you see any objects in the problem? ")
            if(object_response == 'y' or object_response == "yes"): #check if response is affirmative
                object_name = input("What is the object? ") #get the object's name
            else:
                print("No more objects seen...skipping")
                break

            
        #bounds check by modulus the size
        if(equationNumber >= len(eqns)-1):
            equationNumber = equationNumber % len(eqns)
        if(eqns[equationNumber]["var_count"] <= variableNumber):
            variableNumber = variableNumber % eqns[equationNumber]["var_count"]#check for out of bounds
        
        print("variableNumber", variableNumber)
        print("equationNumber", equationNumber)
        variable = eqns[equationNumber]["vars"][variableNumber] #get the variable

        #ask about variable and equation
        response = input(f"Do you know anything about {variable} of {object_name}?")

        knownObjects.append({"object_name": object_name, "objectNumber": objectNumber})

        #append objectNumber, equationNumber, variableNumber, and sequenceNumber into dictionary
        if({"object": objectNumber, "equation": equationNumber, "variable": variableNumber, "sequence": sequenceNumber} not in objectList):
            objectList.append({"Object": objectNumber, "equation": equationNumber,
                            "variable": variableNumber, "sequence": sequenceNumber, "response": response})

    #print the objectList
    for item in objectList:
        print(item, "\n")