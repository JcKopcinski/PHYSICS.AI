import sympy as sp
from function_definitions import *

eqns = {
            0: {
                    "text": "x = x0 + v0 dt + 1/2 a dt^2",
                    "vars": ["x", "x0", "v0", "a", "dt"],
                    "var_count": 5
                },


            1: {
                    "text": "v = v0 + a dt",
                    "vars": ["v", "v0", "a", "dt"],
                    "var_count": 4
            },

            2: {
                    "text": "dt = t - t0",
                    "vars": ["t", "t0"],
                    "var_count": 3
            }
}

if __name__ == "__main__":
    bitString = generate_random_string(27)
    bitList = split_bitstring(bitString)
    print(bitList)
    vals = [int(i, 2) for i in bitList] #convert bitStrings to integers
    print(vals)

    objectList = []
    print(objectList)
    print(len(objectList))
    #asking questions
    for i in range(0, len(vals), ATTRIBUTES):
        if(objectList[vals[i]] == ''):
            object_response = input("Do you see any objects in the problem? ")
            if(object_response == 'y' or object_response == "yes"):
                object_name = input("What is the object? ")
                objectList[vals[i]] = object_name
            else:
                continue
    print(objectList)