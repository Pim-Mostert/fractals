import matplotlib.pyplot as plt; plt.ion()
import numpy as np

import ifs
from importlib import reload; reload(ifs)

fig, ax = plt.subplots(figsize=(6, 6))

# Draw fractal
n_points = 20000

x = np.zeros((2, n_points))

fractal = ifs.BarnsleyFern()

for i in range(0, n_points):
    x[:, i] = fractal.get_next_point()

ax.scatter(x[0, :], x[1, :], s=0.2, color="black")

