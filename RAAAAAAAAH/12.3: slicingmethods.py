import numpy as np

a = np.array([[0,1,2,3,4,5],
     [10,11,12,13,14,15],
     [20,21,22,23,24,25],
     [30,31,32,33,34,35],
     [40,41,42,43,44,45],
     [50,51,52,53,54,55]])

pink = a[1,2:4]
green = a[2:4,4:]
blue = a[:,1]
orange = a[2::2,::2]

print(pink)
print(green)
print(blue)
print(orange)
