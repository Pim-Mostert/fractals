import matplotlib.pyplot as plt; plt.ion()
import numpy as np

from ifs import BarnsleyFern, SierpinskiTriangle
from importlib import reload; reload(BarnsleyFern)

fig, ax = plt.subplots(figsize=(6, 6))

# Draw fractal
n_points = 100000

x = np.zeros((2, n_points))

fractal = BarnsleyFern()

for i in range(0, n_points):
    x[:, i] = fractal.get_next_point()

ax.scatter(x[0, :], x[1, :], s=0.2, color="black")

