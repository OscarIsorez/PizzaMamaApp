 

class Pizza:
    nom = ""
    ingredients = ""
    prix= 0.0
    vegetarienne = False

    def __init__(self, nom ,  ingredients,prix, vegetarienne) -> None:
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne
    

    def get_dictionnary(self):
        return {"nom":self.nom, "ingredients":self.ingredients, "prix":self.prix, "vegetarienne": self.vegetarienne}