# Symbolic Function Approximator
Symbolic function approximator aims to create a function to approximate a data distribution using the symbolic paradigm with programming logic.

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