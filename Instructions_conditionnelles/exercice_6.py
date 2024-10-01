def attaque(dé, votre_santé, santé_adversaire, puissance_attaque):
    if dé <= 2:
        votre_santé = votre_santé / 2
    elif 3 <= dé <= 8:
        santé_adversaire = santé_adversaire - puissance_attaque
    else:
        santé_adversaire = 0
    return votre_santé, santé_adversaire
