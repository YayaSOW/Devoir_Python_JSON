"""
    Creation de la liste & Affichage des elements de la liste:
        - Definition de liste
        - Ajouter methode :
            - ajouter :
                - Erreur si l'element n'est pas une chaine :
                raise ValueError(...),
                - Element ne doit pas exister dans la liste :
                retourner False
                    et afficher un message (Element existe deja)
            - enlever :
                - Retourner True si bien enlever sinon False,
            - afficher :
                - Afficher tous les elements de la liste
"""

class Liste:
    def __init__(self):
        self.elements = []

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("L'élément doit être une chaîne de caractères")
        if element in self.elements:
            print("L'élément existe déjà dans la liste")
            return False
        else:
            self.elements.append(element)
            return True

    def enlever(self, element):
        if element in self.elements:
            self.elements.remove(element)
            return True
        else:
            return False

    def afficher(self):
        print("Éléments de la liste :")
        for element in self.elements:
            print(element)


liste=Liste()
liste.ajouter("Tag Heuer")
liste.ajouter("Hublot")
liste.ajouter("Rolex")
liste.afficher()
liste.ajouter("Rolex")
liste.enlever("Role")
liste.enlever("Rolex")
liste.afficher()