import random

ATTRIBUTES = 3 #object, equation, varaible

#for now, generate_random_string must be an integer multiple of the hyperparameter ATTRIBUTES
def generate_random_string(length): #generate a random string based on input values
    val = ''.join(random.choice(['0', '1']) for i in range(length)) #randomize whether 1 or 0 picked
    return val

def split_bitstring(bit_String): #split a random string into sets of parameters
    return [bit_String[i:i+ATTRIBUTES] for i in range(0, len(bit_String), ATTRIBUTES)] #split the string into a size of ATTRIBUTES

#convert bits into their bitwise values
