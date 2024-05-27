import numpy as np

v = np.array([2, 3])
print(v[0])
print(v[1])

rows = 2
cols = 3
m = np.zeros((rows, cols))

m[0][0] = 2.0
m[1][0] = 3.0
m[0][1] = 5.0

print(m)