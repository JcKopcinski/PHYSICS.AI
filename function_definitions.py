import random

ATTRIBUTES = 4 #object, equation, varaible, sequence

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
                    "vars": ["t", "t0", "dt"],
                    "var_count": 3
            }
}

#for now, generate_random_string must be an integer multiple of the hyperparameter ATTRIBUTES
def generate_random_string(length): #generate a random string based on input values
    val = ''.join(random.choice(['0', '1']) for i in range(length)) #randomize whether 1 or 0 picked
    return val

def split_bitstring(bit_String): #split a random string into sets of parameters
    return [bit_String[i:i+ATTRIBUTES] for i in range(0, len(bit_String), ATTRIBUTES)] #split the string into a size of ATTRIBUTES

def check_tval(object_):
    response = input("Do you know anything about the time interval of " + object_ + "? ")
    if response == "yes" or response == 'y':
        time_interval_description = input("Describe the time interval: ")
        eqns[0]["vars"][4] = time_interval_description
        eqns[1]["vars"][3] = time_interval_description
    return


# def check_position(object_):
#     response = input("Do you know anything about the position of " + object_ + "? ")
#     if response == "yes" or response == 'y':
#         if eqns[1]["vars"][3] is "d" or eqns[0]["vars"][4] is "dt":

#     return

#convert bits into their bitwise values