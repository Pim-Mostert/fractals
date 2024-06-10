import abc
import math
import random
import numpy as np
from typing import List

class IfsFractal(abc.ABC):
    def __init__(self, x0: np.array, transformations: List[np.array]):
        self.x = np.append(x0, np.array([1]))
        self.transformations = transformations
        
    def get_next_point(self):
        next_transformation = random.randint(0, len(self.transformations)-1)
        
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