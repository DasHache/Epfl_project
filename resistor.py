class Resistor:
    
    def __init__(self, resistance):
        self.r = resistance
    
    def __repr__(self):
        return f" generator with {self.p} V as output"
        
    def find_current(self, potential):
        return potential / self.r
    
    def find_potential(self, current):
        return current * self.r
    
    def resistance_serie(self, other):
        NR = Resistor(self.r + other.r)
        return NR
    
    def resistance_parallele(self, other):
        if self.r != 0 and other.r != 0:
            newresistance = 1 / (1/self.r + 1/other.r)    
        
        elif self.r == 0 and other.r == 0:
            return "no resistance, be careful maybe you have an error", 0
        
        elif self.r == 0:
            newresistance = other.r
            
        else:
            newresistance = self.r
        
        RN = Resistor(newresistance)
        return RN