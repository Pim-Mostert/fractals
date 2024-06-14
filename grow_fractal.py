import numpy as np

class Node:
    def __init__(self):
        self.size = 1
        self.children = []
        self.p_new_child = 0.05
        
    def grow(self):
        self.size = self.size + 1
        
        if self._new_child():
            self.children.append(Node())
        else:
            child = self._select_child()       
             
            child.grow()
            
    def _new_child(self):
        if not self.children:
            return True
        
        if np.random.rand(1) < self.p_new_child:
            return True
        
        return False
    
    def _select_child(self):
        i = np.random.choice(len(self.children))
        
        return self.children[i]
    
    def draw(self, axes, x0, M):
        # Draw self
        d = M @ np.array([[0], [self.size]])
        x1 = x0 + d
        
        tmp = np.hstack((x0, x1))
        axes.plot(tmp[0, :], tmp[1, :], linewidth=1)
        
        # Delegate to children
        angles = np.linspace(-np.pi/4, np.pi/4, len(self.children))
        for (i, child) in enumerate(self.children):
            angle = angles[i]
            R = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
            
            child.draw(axes, x1, R)
        
    
            
        
        
    
    