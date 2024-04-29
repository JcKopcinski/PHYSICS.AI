import sympy as sp
from function_definitions import *

NUM_BITS = 27 #number of bits in bitString. (current implementation NUM_BITS must be a divisible integer of ATTRIBUTES)

if __name__ == "__main__":

    bitString = generate_random_string(NUM_BITS)
    bitList = split_bitstring(bitString)

    vals = [int(i, 2) for i in bitList] #convert bitStrings to integers

    objectList = [None] * ((2**ATTRIBUTES)) #initialize object list to empty

    #-------------------------DEBUG------------------
    print("bitString: " + bitString)
    print(bitList)
    print(vals)
    print(objectList)
    #-------------------------DEBUG------------------

    #BUILD OBJECT LIST ----- MOVE TO FUNCTION
    for i in vals[::3]: #use list slicing to find each set
        if not objectList[i] and i == vals[0]: #check if there is an object at this position of the set
            object_response = input("Do you see any objects in the problem? ") #ask about the object
            if(object_response == 'y' or object_response == "yes"): #check if response is affirmative
                object_name = input("What is the object? ")
                objectList[vals[i]] = object_name #set the object name
                
            else:
                break
        else:
            object_response = input("Do you see any more objects in the problem? ") #ask about the object
            if(object_response == 'y' or object_response == "yes"): #check if response is affirmative
                object_name = input("What is the object? ")
                objectList[vals[i]] = object_name
            else: #exit if no more objects in problem
                break
    if all(obj is None for obj in objectList): #no information on object provided by user
        print("No objects were provided. Exiting program.")
        exit()
    #----------------------------------------
    
    print(objectList)