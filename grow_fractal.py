import numpy as np

class Node:
    def __init__(self):
        self.size = 1
        self.children = []
        self.p_new_child = 0.05
        
    def grow(self):
        self.size = self.size + 1
        
        if self.new_child():
            self.children.append(Node())
        else:
            child = self.select_child()       
             
            child.grow()
            
    def new_child(self):
        if not self.children:
            return True
        
        if np.random.rand(1) < self.p_new_child:
            return True
        
        return False
    
    def select_child(self):
        i = np.random.choice(len(self.children))
        
        return self.children[i]
    
    def draw(x, 
    
            
        
        
    
    