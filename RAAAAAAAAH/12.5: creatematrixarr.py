import numpy as np

def set_array(L, rows, cols):
    new = np.empty((rows,cols))
    x = 0
    for i in range(rows):
        for j in range(cols):
            new[i,j] = L[x]
            x+=1
    return new

list1 = [1,2,3,4,5,6,7,8,9,10]
print(set_array(list1, 5, 2))
