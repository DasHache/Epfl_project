import resistor as res
import generator as ge

def cc():
    I = 0
    L = ["Ug", "resistance", "courant"]
    l = len(L) 
    for i in range(l):
        a = input(f"connaissez vous le/la {L[i]} du circuit ? 'value' or 'no'")
        if a != "no":
            if i == 0:
                G = ge.Generator(float(a))
            if i == 1:
                R = res.Resistor(float(a))
            if i == 2:
                I = float(a)
                
                
    b = input("que cherchez-vous ?")
    
    for i in range(l):
        if b == "courant":
            I = R.find_current(G.ret_potentiel())
            return I
        if b == "potentiel":
            Ug = R.find_potential(I) 
            return Ug
        if b == "resistance":
            R = G.find_resistance(I)
            return R
        
print(cc())
