class Resistor:
    
    def __init__(self, resistance):
        self.r = resistance
    
    def __repr__(self):
        return f" generator with {self.p} V as output"
        
    def find_current(self, potential):
        return potential / self.r
    
    def find_potential(self, current):
        return current * self.r
    
#find if it is possible to indicate an attribute which is not always known
#for example for potential and current