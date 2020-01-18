from expressions import *
from gene import *

chro = []

""" Example chromosome
chro = [
    ['I', ['v1', '0']],
    ['O', ['v2', 'v1', '+', 'v2']],
    ['C', ['v2', '<', 'v1', [['I', ['v3', '0']]]]],
]
"""

f1 = Function('f1', chro)
print(str(f1))

# print("ini")
# gene = f1.c_initialise()
# f1.chro.append(gene)
# print("if")
# gene = f1.c_if()
# f1.chro.append(gene)
# print("assign")
# gene = f1.c_assign()
# if gene: f1.chro.append(gene)
# f1.exp_lst = f1.create_exp_lst(f1.chro, new=False)
# f1.func_str = f1.create_func()
# print(str(f1))

for i in range(100):
    f1.mutate()

print(str(f1))
for s, v in f1.stats.items():
    print(s,v)

exec(str(f1))
a = f1(1)
print(a)