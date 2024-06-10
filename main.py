import matplotlib.pyplot as plt; plt.ion()
import numpy as np
from ifs import SierpinskiTriangle

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Draw fractal
n_points = 10000

x = np.zeros((2, n_points))

sierpinski = SierpinskiTriangle()

for i in range(0, n_points):
    x[:, i] = sierpinski.get_next_point()

ax.scatter(x[0, :], x[1, :], s=1, color="black")
