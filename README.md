# PHYSICS.AI

# 24-April-2014

* Justin: keep working on code and getting the questions asked, as dictated by the binary string.

* Think about a data structure to keep track of the student's answers.

* Stored answers should consist of 4 itenms
    # The object number asked about
    # The equation number asked about
    # The variable in the equation asked about
    # The student's response

* For stoing answers, I'd recommend a list of dictionaries.  The list can grow and store each answers, and each dictionary in the list will be an answer.  

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
