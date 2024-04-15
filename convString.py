import sympy as sp
import random

class EqTable: 
    def __init__(self):
        self.EQUATIONS = {} #initialize to empty

    #add an equation to the dictionary
    def add_equation(self, equation):
        #split equation across = sign; necessary for sympy parsing
        left, right = equation.split("=")
        varsLeft = sp.sympify(left).free_symbols #parse left side of equation
        varsRight = sp.sympify(right).free_symbols #parse right side of equation
        self.EQUATIONS[equation] = varsLeft.union(varsRight) #combine variables from left and right

    #remove an equation from the dictionary
    def remove_equation(self, equation):
        if(equation in self.EQUATIONS):
            del self.EQUATIONS[equation]
        else:
            raise ValueError("failed to remove equation")

    #get the list of variables of a specific equation
    def get_variables(self, equation):
        return self.EQUATIONS.get(equation, [])
    
    #print the table, useful for debugging
    def print_table(self):
        for equation, variables in self.EQUATIONS.items():
            print(f"Equation: {equation}, Variables: {variables}")

def generate_random_string(length):
    randomBinaryString = ''.join(random.choice(['0', '1']) for i in range(length)) #randomize whether 1 or 0 picked

    return [randomBinaryString[i:i+3] for i in range(0, len(randomBinaryString), 3)] #split the string into 3

string_ = generate_random_string(27);
print(string_)

EquationTable = EqTable() #initialize equation table
EquationTable.add_equation("x = x0 + v0x*Dt +(1/2)*(ax*(Dt**2))")
EquationTable.add_equation("vx = v0x + ax*Dt")

EquationTable.print_table()

#Thoughts: 
    #1. A standard way of configuring each additional equaiton added to the dictionary,
    #to help expansion of eqution table down the line
    #3. Defined constant variables (ie, g = -9.8 ect)
    #4. Global Representation of values. A Dt in one equation should be the same as a Dt in another equation
