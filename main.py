import sympy as sp
from function_definitions import *

NUM_BITS = 36 #number of bits in bitString. (current implementation NUM_BITS must be a divisible integer of ATTRIBUTES)

if __name__ == "__main__":

    bitString = generate_random_string(NUM_BITS)
    bitList = split_bitstring(bitString)

    vals = [int(i, 2) for i in bitList] #convert bitStrings to integers

    objectList = [] #initialize object list to empty


    #-------------------------DEBUG------------------
    print("bitString: " + bitString)
    print(bitList)
    print(vals)
    print(objectList)
    #-------------------------DEBUG------------------

    #count by 3 on each iteration
    for i in range(0, len(vals), 4):
        objectNumber = i
        equationNumber = vals[i+1]
        variableNumber = vals[i+2]
        sequenceNumber = vals[i+3]

        object_response = input("Do you see any objects in the problem? ") #ask about the object
        if(object_response == 'y' or object_response == "yes"): #check if response is affirmative
            object_name = input("What is the object? ") #get the object's name
        else:
            print("No object seen...exiting")
        #get variable and equation
        print("variableNumber: ", variableNumber)
        print("equationNumber: ", equationNumber)

        #bounds check by modulus the size
        if(equationNumber > len(eqns)-1):
            equationNumber = equationNumber % len(eqns)
        if(eqns[equationNumber]["var_count"] < variableNumber):
            variableNumber = variableNumber % eqns[equationNumber]["var_count"] #check for out of bounds
        
        variable = eqns[equationNumber]["vars"][variableNumber] #get the variable
        equation = eqns[equationNumber]["text"] #get the equation

        #ask about variable and equation
        response = input(f"Do you know anything about {variable} of {object_name}?")

        #ask for variable and equation number
        objectList.append({"Object": objectNumber, "equation": equationNumber,
                            "variable": variableNumber, "sequence": sequenceNumber, "response": response})
        #dictionary with 3 key value pairs

    for item in objectList:
        print(item, "\n")