# Symbolic Function Approximator
Symbolic function approximator aims to generate a function using a genetic algorithm to approximate a data distribution using the symbolic paradigm with programming logic.

# Motive
In the debate between symbolic and connectionist paradigms of artificial intelligence (AI), while connectionist neural networks have been popular, some argue that symbolic methods are still necessary to advance the state of AI.

# Methodology
Programming expressions (variable assignments, operations, conditionals, loops) are created, modified or deleted as 'mutations'. With the predictive capacity as the fitness function, the evolutionary algorithm selects for the best functions to pass on favourable programming expressions to the next generation.

# List of Mutations
* Create
    * Initialise new variables
    * Assign variables with operator function
    * Create if-else conditional
        * Create new expression
    * Create for-loop
* Modify
    * Mutate variable values
    * Change operator functions
    * Change if-else inequality
    * Change for-loop start, end, increment values
* Delete existing expressions

# Fitness Function
* Prediction Error = |Predicted Output - Test Output|

# Seed Function
```
def f0(v0):
    return v0
```

# Generated Evolved Functions
* Generations: 200
* Children per generation: 50
```python
def f0(v0):
	v1 = 1
	v0 = mod(v0, v0)
	v2 = v0 + v0
	v2 = div(v0, v1)
	v4 = v2 + v0
	v0 = v0 + v2
	v4 = div(v1, v0)
	v4 = div(v1, v2)
	v1 = v4 * v2
	v1 = v2 + v0
	v5 = v4 - v1
	return v0

def f1(v0):
	v0 = mod(v0, v0)
	v1 = v0 - v0
	v3 = 6
	v1 = v0 + v0
	if v0 < v0:
		if v1 > v0:
			v0 = div(v1, v0)
	v1 = v1 - v1
	v3 = mod(v0, v1)
	v1 = mod(v1, v1)
	v2 = div(v1, v0)
	v9 = -4
	v8 = mod(v0, v0)
	v5 = v8 - v1
	v2 = v8 * v9
	v12 = v2 + v5
	v0 = mod(v12, v1)
	v15 = 0
	v5 = v1 - v0
	return v0
```

# Considerations
1. Variables that have not be defined must not be accessed before definition.
    ```
    v0 = 0
    v2 = v1
    v1 = 1
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    NameError: name 'v1' is not defined
    ```
2. Variables that are initialised within an if-else conditional must not be accessed if the conditional has not been run.
    ```
    v1 = 0
    v0 = 1
    if v1 > v0:
        v2 = 0
    v3 = v2
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
    NameError: name 'v2' is not defined
    ```
3. Division / and modulo % must address ZeroDivisionError.
    ```
    v0 = 0
    v1 = v0 / v0
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    ZeroDivisionError: division by zero
    ```
4. Conditionals (if-else) must track number of indents.
    ```
    v0, v1 = 0, 1
    if v0 > 0:
    if v1 > 1:
            v2 = 3
    File "<stdin>", line 3
        if v1 > 1:
         ^
    IndentationError: expected an indented block
    ```
5. Deletion of variables must consider downstream access of deleted variables.
    ```
    # v1 = 0
    v1 = v0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'v0' is not defined
    ```
