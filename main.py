import matplotlib.pyplot as plt; plt.ion()
import matplotlib; 
import numpy as np

import grow_fractal as pf
from importlib import reload; reload(pf)

node = pf.Node()

for i in range(100):
    node.grow()
    


