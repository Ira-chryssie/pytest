class compte_bancaire:
    def __init__(self,titulaire , sold=0):
        self.titulaire = titulaire
        self.sold = sold
    def deposer(self, montant):
        if montant > 0 :
            self.sold += montant
            print(f"{montant}$deposes sur le compte de {self.titulaire} ")
        else:
            print("le montant a deposer doit etre positif.")
    def retirer(self,montant):
        if montant <=0 :
            print(" le montant a retire doit etre positif.")
        elif montant > self.solde:
            print(" retrait impossible solde insufissant.")
        else:
            self.sold -= montant
            print(f"{montant}$retires du compte de {self.titulaire}.")
    def afficher_solde(self):
        print(f"solde du compte de {self.titulaire} : {self.sold}")

