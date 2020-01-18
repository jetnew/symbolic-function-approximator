"""
Mutation list
* Create
    * Initialise new variables
    * Assign variables with operator function
    * Create if-else condition
        * Create new expression
* Modify
    * Mutate variable values
    * Change operator functions
    * Change if-else inequality
* Delete existing expressions
"""
probabilities = {
    'create': 0.05,
    'modify': 1.0,
    # 'delete': 1.0,
}

create = {
    'initialise': 0.2,
    'assign': 0.95,
    'if': 1.0,
}

modify = {
    'variable': 0.7,
    'operator': 0.9,
    'if': 1.0,
}