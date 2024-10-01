def puissance_ball_ombre(type_adversaire):
    puissance_initiale = 80
    if type_adversaire in ["Psy", "Spectre"]:
        return puissance_initiale * 2
    elif type_adversaire == "Ténèbres":
        return puissance_initiale * 0.5
    elif type_adversaire == "Normal":
        return 0
    else:
        return puissance_initiale