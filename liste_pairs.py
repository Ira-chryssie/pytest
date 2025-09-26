def filtrer_pairs(liste_nombres):
    return [n for n in liste_nombres if n % 2 == 0]
entree = input("ecris une liste de nombres separes par des espaces : ")
liste = [int(x) for x in entree.split()]
print("les nombres pairs sont :", filtrer_pairs(liste))