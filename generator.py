class Generator:
    def __init__(self, potentiel):
        self.p = potentiel
        
    def __repr__(self):
        return f" generator with {self.p} V as output"
    
    def find_resistance(self, current):
        return self.p /current
    
    def ret_potentiel(self):
        return self.p
    
