import numpy as np

# Define the vector
v = np.array([2., 2., 4.])

# Define the unit vectors along the coordinate axes
e0 = np.array([1, 0, 0])
e1 = np.array([0, 1, 0])
e2 = np.array([0, 0, 1])

# Calculate the projections
proj_e0 = np.dot(v, e0)
proj_e1 = np.dot(v, e1)
proj_e2 = np.dot(v, e2)

print(proj_e0)  # Expected output: 2.0
print(proj_e1)  # Expected output: 2.0
print(proj_e2)  # Expected output: 4.0
