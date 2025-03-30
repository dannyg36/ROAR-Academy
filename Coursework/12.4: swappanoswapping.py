import numpy as np

axe = np.array([[0,1,2,3,4,5],
     [10,11,12,13,14,15],
     [20,21,22,23,24,25],
     [30,31,32,33,34,35],
     [40,41,42,43,44,45],
     [50,51,52,53,54,55]])

def swap_rows(M, a, b):
    if type(M) != np.ndarray:
        return "M is not an array"
    elif type(a) != int or type(b) != int:
        return "A or B not an int"
    elif (a < 0 or a >= len(M[0,:])) or (b < 0 or b >= len(M[0,:])):
        return "A or B out of bounds"
    else:
        temp = np.copy(M[a])
        M[a] = M[b]
        M[b] = temp

swap_rows(axe,0,1)
print(axe)
swap_rows(axe,0,1)

def swap_cols(M, a, b):
    if type(M) != np.ndarray:
        return "M is not an array"
    elif type(a) != int or type(b) != int:
        return "A or B not an int"
    elif (a < 0 or a >= len(M[:,0])) or (b < 0 or b >= len(M[:,0])):
        return "A or B out of bounds"
    else:
        temp = np.copy(M[:,a])
        M[:,a] = M[:,b]
        M[:,b] = temp

swap_cols(axe,0,1)
print(axe)
swap_cols(axe,0,1)