from evaluation import *
from expressions import *
from gene import *

chro = []
selected = Function('f'+str(i), chro)
for i in range(1000):
    if i % 20 == 0:
        print("Generation:", i)
    # Mutate
    selected.mutate()
    chro = selected.chro

    # Generate functions
    fns = [Function('f'+str(i), chro) for i in range(50)]
    fn_arr = [str(f) for f in fns]

    # Batch test
    error_arr = test_loop(fn_arr, index, increment_two, n=100)
    min_error = min(error_arr)
    idx = error_arr.index(min_error)

    # Best performing
    selected = fns[idx]

print(selected)
print("Error:", min_error)