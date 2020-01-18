import matplotlib.pyplot as plt
from evaluation import *
from main import *

plt.plot(increment_two, c='r')

output, error = test(str(selected), index, increment_two, n=100)
print("Error:", error)
plt.plot(output)
plt.show()
