class Produit :
    def __init__(self,nom:str,prix:float,description:str):
       self.nom=nom
       self.prix=prix
       self.description=description
    def info_poduit(self):
           print("les infos complet du produits:",self.nom,self.prix,self.description)    
    def modifier_prix(self,nouveau_prix:float):
       self.prix=nouveau_prix
       print("le nouveau prix est:",self.prix)
    def mis_a_jour(self,nouveau_description:str): 
       self.description =nouveau_description
       print("la nouvelle description est:",self.description)
       
P1=Produit ("Lait",1500.0,"contient des vitamines")
P1.info_poduit()
# print("Nom:",P1.nom ,"PRIX",P1.prix ,"DESCRIPTION",P1.description )
P1.modifier_prix(2000.0)
P1.mis_a_jour("Notre lait est fait a base de lait de vache")