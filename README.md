# PHYSICS.AI

# 24-April-2014

* Justin: keep working on code and getting the questions asked, as dictated by the binary string.

* Think about a data structure to keep track of the student's answers.

* Stored answers should consist of 4 itenms
    1. The object number asked about
    1. The equation number asked about
    1. The variable in the equation asked about
    1. The student's response

## Storing answers
* For storing answers, I'd recommend a list of dictionaries.  The list can grow and store each answer, and each dictionary in the list will be a given answer.  

* Suppose we call our list of knowns `knowns`. Initially it'll start empty like

```
knowns = []
```

With each answer that comes in, we'll store the object #, equation #, variable #, and student response. After a couple of questions, `knowns` might look like this:


```python
knowns = [
            {"object": 3, "equation": 2, "variable": 1, "response": "the speed of the stone after it accelerated"},
            {"object": 5, "equation": 1, "variable": 2, "response": "it says the the truck is initally at x=0"}
]
```

Such a structure will also make it each to scan and avoid asking the same question again.  So if the binary string comes up with object=3, equation=2, and variable=1, we can avoid asking it, since this question has already been asked and answered.

## Keeping numbers in range

If a number from the binary string is out of range, for example, it want to ask about equation 7, but we only have 3 equations, you can do this

1. ignore the request
2. Do a `equation_num = equation_num % max_equations` Here the `%` is the modulus operator, which returns the remainder of a division, which will always be a number between `0...max_equations`.

Assuming we have something like

```python
eqns = {
            0: {
                    "text": "x = x0 + v0 dt + 1/2 a dt^2", 
                    "vars": ["x", "x0", "v0", "a", "dt"],
                    "var_count": 5,
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
```

we can say `max_equations = len(eqns)`

## Contraints

I'll keep working on the contraint warning logic and code in the file called `constraints.py.`
