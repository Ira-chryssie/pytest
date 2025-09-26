def calculer_moyenne(notes):
    total = 0
    compteur = 0
    for note in notes:
        if isinstance(note, (int,float)):
            total +=note
            compteur+=1
    if compteur == 0:
        return 0
    return total/compteur
entree = input("entrez les notes separees par des virgules : ")
#transformer le texte en liste
notes_utilisateurs = []
for valuer in entree.split(","):
    valuer = valuer.strip() #enlever les espaces
    try:
        notes_utilisateurs.append(float(valuer))#comvertir en nombre
    except valueerror: # si c'est pas un nombre on l'ignore
     continue
#utiliser la fonction
moyenne = calculer_moyennne(notes_utilisateurs)
print("la moyenne est : ", moyenne)