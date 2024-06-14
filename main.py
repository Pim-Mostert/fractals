import matplotlib.pyplot as plt; plt.ion()
import numpy as np

import grow_fractal as pf
from importlib import reload; reload(pf)

node = pf.Node()

for i in range(1000):
    node.grow()

fig = plt.figure()
axes = plt.gca();
axes.axis('equal')
node.draw(plt.gca(), np.zeros((2, 1)), np.eye(2))

