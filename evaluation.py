import numpy as np

############# UTILS ##############

def execute(fn_str, v0):
    """Function string must take in specific variable names v0 as input and result as output."""
    ll = locals()
    exec(fn_str, globals(), ll)
    return ll["v0"]

def test(fn_str, input_array, test_array, n=100):
    output_array = []
    input_array = input_array[:n]
    test_array = test_array[:n]
    for v0 in input_array:
        result = execute(fn_str, v0)
        # print(result)
        output_array.append(result)
    # print(output_array)
    error = np.sum(np.absolute(np.subtract(output_array, test_array)))
    return output_array, error

def test_loop(fn_arr, input_array, test_array, n=100):
    error_arr = []
    input_array = input_array[:n]
    test_array = test_array[:n]
    for fn_str in fn_arr:
        _, error = test(fn_str, input_array, test_array, n=n)
        error_arr.append(error)
    return error_arr




############# TEST SEQUENCES ##################
n = 100

index = [i for i in range(n)]
increment_one = [i for i in range(n)]
increment_two = [i*2 for i in range(n)]

fib = [0,1]
for i in range(n-2):
    fib.append(fib[i] + fib[i+1])
