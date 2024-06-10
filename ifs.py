import abc
import math
import numpy as np
from typing import List

class IfsFractal(abc.ABC):
    def __init__(self, x0: np.array, transformations: List[np.array], p=None):
        self.x = np.append(x0, np.array([1]))
        self.transformations = transformations
        self.p = p if p is not None else np.ones((len(transformations)))/len(transformations)
        
    def get_next_point(self):
        next_transformation = np.random.choice(range(0, len(self.transformations)), p=self.p)
        
        self.x = self.x @ self.transformations[next_transformation]
        
        return self.x[:2]
        
class SierpinskiTriangle(IfsFractal):
    def __init__(self):
        x0 = np.array([0, 0])
        
        t1 = np.array([[0.5, 0, 0], [0, 0.5, 0], [0, 0, 1]])
        t2 = np.array([[0.5, 0, 0], [0, 0.5, 0], [0.5, 0, 1]])
        t3 = np.array([[0.5, 0, 0], [0, 0.5, 0], [0.25, math.tan(math.pi/3)*0.25, 1]])
        
        transformations = [t1, t2, t3]
                
        super().__init__(x0, transformations)
        
class BarnsleyFern(IfsFractal):
    def __init__(self):
        x0 = np.array([0, 0])
        
        t1 = np.array([[0, 0, 0], 
                       [0, 0.16, 0], 
                       [0, 0, 1]])
        t2 = np.array([[0.85, -0.04, 0], 
                       [0.04, 0.85, 0], 
                       [0, 1.6, 1]])
        t3 = np.array([[0.2, 0.23, 0], 
                       [-0.26, 0.2, 0], 
                       [0, 1.6, 1]])
        t4 = np.array([[-0.15, 0.26, 0], 
                       [0.28, 0.24, 0], 
                       [0, 0.44, 1]])
        
        transformations = [t1, t2, t3, t4]
        
        p = [0.01, 0.85, 0.07, 0.07]

        super().__init__(x0, transformations, p)