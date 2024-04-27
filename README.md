# PHYSICS.AI

# 24-April-2014

* Justin: keep working on code and getting the questions asked, as dictated by the binary string. It think it's all on the right track.

* Also: I was thinking about your function that explicitly asks about time information.  Try to base your code around the logic of relying solely on the binary string to determine what question to ask, about what object, equation, and variable.  See the equation data-structure below, where certainly the binary string will ask about variables in equation 2 (the `dt=t-t0` equation).

* It is possible that at some point, your code will run out of questions to ask.  This is when we'll run the optimizer through forward step, which will generate a new set of binary strings, a bit closer to the solution.


## Storing answers

* Think about a data structure to keep track of the student's answers.

* Stored answers should consist of 4 items
    1. The object number asked about
    1. The equation number asked about
    1. The variable in the equation asked about
    1. The student's response

* For storing answers, maybe a list of dictionaries will work.  The list can grow to store each answer. Each dictionary in the list is a given answer.  

* Suppose we call our list of knowns `knowns`. Initially it'll start empty like

```python
knowns = []
```

With each answer that comes in, we'll store the object #, equation #, variable # asked about, and the student's response. After a couple of questions, `knowns` might look like this:


```python
knowns = [
            {"object": 3, "equation": 2, "variable": 1, "response": "the speed of the stone after it accelerated"},
            {"object": 5, "equation": 1, "variable": 2, "response": "it says the the truck is initally at x=0"}
]
```

Such a structure will also make it easy to scan for the purpose of avoiding asking the same questions again and again.  So if the binary string comes up with object=3, equation=2, and variable=1, we can avoid asking it, since an answer to this question is already in the `knowns` structure.

## Keeping numbers in range

If a number from the binary string is out of range, for example, it wants to ask about equation 7, but we only have 3 equations, you can do this

1. Ignore the request and just go on to the next one.

2. Suppose `equation_num` came right off of the binary string. Do a 

```python
equation_num = equation_num % max_equations
```

Here the `%` is the "modulus operator," which returns the remainder of the division of the two arguments, which here will always be a number between `0...max_equations`.

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
                    "vars": ["t", "t0","dt"],
                    "var_count": 3
            }
}
```

we can say `max_equations = len(eqns)`

## Contraints

I'll keep working on the contraint warning logic and code in the file called `constraints.py.` Like I said, I'll give you a function like `warn()` that will return `False` if you should not accept a student's 'yes' answer to a question.