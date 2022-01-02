import resistor as res
import generator as ge

def creation_circuit():
    Intensité = 0
    Liste = ["Ug", "resistance", "courant"]
    longueur = len(Liste) 
    ii = 0
    
    for i in range(longueur):    
        a = input(f"connaissez vous le/la {Liste[i]} du circuit ? 'value' or 'no'")
        if a != "no":
            if i == 0:
                G = ge.Generator(float(a))
            if i == 1:
                R = res.Resistor(float(a))
            if i == 2:
                Intensité = float(a)
        else:
            ii = i
    
    if Liste[ii] == "courant":
        Intensité = R.find_current(G.ret_potentiel())
        return Intensité
    if Liste[ii] == "potentiel":
        Ug = R.find_potential(Intensité) 
        return Ug
    if Liste[ii] == "resistance":
        R = G.find_resistance(Intensité)
        return R
        
print(creation_circuit())
