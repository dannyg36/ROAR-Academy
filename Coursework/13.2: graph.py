import matplotlib.pyplot as plt
import os
import numpy as np

x1 = np.arange(1, 2, 0.005)
x2 = np.arange(2, 3, 0.005)

y1 = x1*2
y2 = 10-(x2*3)

plt.plot(x1, y1, color = 'b', linewidth = 2)
plt.plot(x2, y2, color = 'b', linewidth = 2)

plt.ylim(1, 4)
plt.xlim(1, 3)

plt.xticks(np.arange(1,3.5,0.5), ['1.0', '1.5', '2.0', '2.5', '3.0'])

plt.title("Sample graph!")
plt.xlabel("x - axis")
plt.ylabel("y - axis")

plt.show()