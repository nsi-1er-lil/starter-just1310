def puissance_finale_subie(puissance_initiale, type_attaque):
    if type_attaque in ["Acier", "Électrique", "Vol"]:
        return puissance_initiale / 2
    elif type_attaque == "Sol":
        return puissance_initiale * 2
    else:
        return puissance_initiale