def compter_voyelles(texte):
    voyelles = "aiuoeyAIUOEY"
    compteur = 0
    for lettre in texte:
        if lettre in voyelles:
            compteur += 1
    return compteur
texte = input("Entrez une chaine de caractere : ")
nb_voyelle = compter_voyelles(texte)
print ( "le nombre de voyelle = ", nb_voyelle)
