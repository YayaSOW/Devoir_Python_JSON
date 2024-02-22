import json
import os
from tabulate import tabulate

file="./devoir.json"

def saisiUtilisateur()->dict:
    while True:
        try:
            id=int(input("ID:\n"))
            break
        except ValueError:
            print("Vous a ecrit un caractère !")
    nom=input("Nom:\n")
    prenom=input("Prenom:\n")
    email=input("Email:\n")
    motDePasse=input("Mot De Passe:\n")
    utilisateur={
            "id":id,
            "nom":nom,
            "prenom":prenom,
            "email":email,
            "motDePasse":motDePasse
        }
    return utilisateur

def saisiCategorie(idP:int)->dict:
    libelle=input("La catégorie du libelle:\n")
    categorie={
        "libelle": libelle,
        "id": idP
    }
    return categorie

def saisiProduit()->dict:
    libelle=input("libelle:\n")
    while True:
        try:
            prix=int(input("Prix:\n"))
            break
        except ValueError:
            print("Vous a ecrit un caractère !")
    while True:
        try:
            quantite=int(input("Quantite:\n"))
            break
        except ValueError:
            print("Vous a ecrit un caractère !")
    dateDePeremption=input("Date De Peremption:\n")
    while True:
        try:
            id=int(input("ID:\n"))
            break
        except ValueError:
            print("Vous a ecrit un caractère !")
    categorie=saisiCategorie(id)
    newProduct={
                "libelle": libelle,
                "prix": prix,
                "quantite": quantite,
                "categorie": categorie,
                "dateDePeremption": dateDePeremption if dateDePeremption else None,
                "id": id
            }
    return newProduct


def readOnly(path)->list:
    try:
        with open(path,"r") as f:
            contenu=json.load(f)
            return (contenu)
    except:
        print("Fichier Introuvable!!!")

def seConnecter(path):
    utilisateur=saisiUtilisateur()
    if(os.path.exists(path)):
        with open (path,"r") as f:
            contenu=json.load(f)
            for i in contenu:
                (i["utilisateurs"]).append(utilisateur)
        with open (path,"w") as f1:
            json.dump(contenu,f1,indent=4)
    else:
        with open (path,"w") as f1:
            json.dump([utilisateur],f1,indent=4)


def addNewProduit(path):
    newProduct=saisiProduit()
    if(os.path.exists(path)):
        with open(path,"r") as f:
            contenue=json.load(f)
            for i in contenue:
                (i["catalogue"]["produits"]).append(newProduct)
        with open(path,"w") as f1:
            json.dump(contenue,f1,indent=4)
    else:
        with open(path,"w") as f:
            json.dump(newProduct,f,indent=4)

head=["ID","Libelle","Prix"]
head1=["ID Commande","ID Produit","Libellé","Qunatité Vendu","Prix"]

def addNewVente(path, vente:object):
    if(os.path.exists(path)):
        with open(path,"r") as f:
            contenu=json.load(f)
            for i in contenu:
                i["ventes"].append(vente)
        with open(path,"w") as f1:
            json.dump(contenu,f1,indent=4)
    else:
        with open(path,"w") as f:
            json.dump(vente,f,indent=4)

def createSend(path):
    liste=[]
    with open(path,"r") as f:
        contenu=json.load(f)
        produits=contenu[0]["catalogue"]["produits"]
        print("{:.^70}".format("Bienvenue sur Notre Catalogue De Vente👇"))
        for produit in produits:
            p1=((produit["id"]),(produit["libelle"]),(produit["prix"]))
            liste.append(p1)
        writeTable(liste)
        numTableau=listeNum(liste)
        print("Faites votre choix svp!!!")
        val=""
        while val not in numTableau:
            try:
                val=int(input("Veuillez saisir l'id de votre choix:\n"))
            except ValueError:
                print("Erreur de caractère!")
        while True:
            try:
                qtte=int(input("Quelle Quantité ? :\n"))
                break
            except ValueError:
                print("Erreur de caractère!")
        for produit in produits:
            if(val==produit["id"]):
                if (qtte>(produit["quantite"])):
                    print("Désolé Quantité de stock insuffisante💀 \n")
                    print("Reste : {}".format(produit["quantite"]))
                else:
                    while True:
                        try:
                            id=int(input("Id de la Vente:\n"))
                            break
                        except ValueError:
                            print("Vous avez saisie un caracteur!")
                    vente={
                        "id": id,
                        "idProduit": produit["id"],
                        "qunatiteVendu": qtte,
                        "prixDeVente": qtte*(produit["prix"])
                    }
                    produit["quantite"]-=qtte
                    addNewVente(file,vente)


def writeTable(listeProduit:list, header=head) -> None:
    data = [i for i in listeProduit]
    print(tabulate(data,headers=header,tablefmt="rounded_grid"))

def listeNum(liste:list)->list:
    num=[]
    for i in liste:
        num.append(i[0])
    return num

def getVenteByCommande(listeIdVente,contenuVente)->list:
    panierVente=[]
    idProduit=[]
    for i in contenuVente:
        if (i["id"] in listeIdVente):
            p1=((i["id"]),(i["idProduit"]),(i["quantiteVendu"]),(i["prixDeVente"]))
            panierVente.append(p1)
            idProduit.append(i["idProduit"])
    return panierVente,idProduit


def getProduitByVente(listeIdProduit,contenuProduit):
    panierProduit=[]
    for i in contenuProduit:
        if (i["id"] in listeIdProduit):
            panierProduit.append((i["libelle"]))
    return panierProduit

def fusionListTupleEtListe(listetuple:list, liste:list)->list:
    for i in range(len(listetuple)):
        listetuple[i]=listetuple[i][:2]+(liste[i],)+listetuple[i][2:]
    return listetuple

def afficheDetailCommande(path,idUser):
    idVente=[]
    contenues=readOnly(path)
    for i in contenues: 
        contenuCommande=i["commandes"]
        contenuVente=i["ventes"]
        contenuProduit=i["catalogue"]["produits"]
    for commande in contenuCommande:
        if (idUser == (commande["idUtilisateur"])) :
            listeIdVente=(commande["tableauDeVente"])
            for i in listeIdVente:
                idVente.append(i)
            print("{:.^75}".format("Les détails de votre commande sont:"))
            detail,listeIdProduit=getVenteByCommande(listeIdVente,contenuVente)
            listeLibelleP=getProduitByVente(listeIdProduit,contenuProduit)
            print(detail)
            print(listeLibelleP)
            descriptionV=fusionListTupleEtListe(detail,listeLibelleP)
            print(len(descriptionV))
            writeTable(descriptionV,head1)


# afficheDetailCommande(file,100)
# createSend(file)


def createCatalogue():
    db=readOnly(file)
    print(db)

# createCatalogue()