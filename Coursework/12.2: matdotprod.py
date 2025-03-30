import numpy as np

a = np.array([[6,-9,1],[4,24,8]])
b = a*2
print(b) #debug

x = np.array([[1,0],[0,1]])
y = np.dot(x,a) #dot prod of the two arrays
print(y)

q = np.array([[4,3],[3,2]])
w = np.array([[-2,3],[3,-4]])
m = np.dot(q,w)
print(m)