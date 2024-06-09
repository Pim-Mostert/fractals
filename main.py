import random
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Draw fractal
n_points = 10000

x = np.zeros(n_points)
y = np.zeros(n_points)

for i in range(1, n_points):
    next_transformation = random.randint(0, 2)
    
    if next_transformation == 0:
        x[i] = x[i - 1] * 0.5
        y[i] = y[i - 1] * 0.5
    elif next_transformation == 1:
        x[i] = x[i - 1] * 0.5 + 0.5
        y[i] = y[i - 1] * 0.5
    elif next_transformation == 2:
        x[i] = x[i - 1] * 0.5 + 0.25
        y[i] = y[i - 1] * 0.5 + 0.4330127018922192
    # elif next_transformation == 2:
    #     x[i] = x[i-1] * 0.5 + 0.5
    #     y[i] = y[i-1] * 0.5 + 0.5

ax.plot(x, y, "o", markersize=1, color="black")
