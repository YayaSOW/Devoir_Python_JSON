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
    except FileNotFoundError:
        print("Fichier introuvable!!!")


def writeOnly(path,value)->None:
    if (os.path.exists(path)):
        with open(path,"w") as f:
            json.dump([value],f,indent=4)
    else:
        with open(path,"w") as f:
            json.dump(value,f,indent=4)

def creerUtilisateur(path):
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
def seConnecter1(email,mdp):
    utilisateurConnect=[]
    contenu=readOnly(file)
    for i in contenu:
        utilisateurs=(i["utilisateurs"])
        for utilisateur in utilisateurs:
            if (utilisateur["email"] == email and utilisateur["motDePasse"] == mdp):  
                print(utilisateur)
                utilisateurConnect.append(utilisateur)
                contenu[0]["utilisateurConnect"]=utilisateur
        if(not(utilisateurConnect)):
            print("email ou mot de passe incorrect")
        else:
            writeOnly(file,contenu)

def deconnecter(email,mdp):
    utilisateurConnect=[]
    contenu=readOnly(file)
    allData=contenu[0]
    utilisateur=allData.get("utilisateurConnect")
    if(not(utilisateur)):
        print("Connecter vous d'abord!!!")
    else:
        print(utilisateur["email"],utilisateur["motDePasse"])
        if(utilisateur["email"] == email and utilisateur["motDePasse"] == mdp):
            print("vous etes deconnecter")
            del contenu[0]["utilisateurConnect"]
            writeOnly(file,contenu)


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
    # print(contenuProduit)
    for commande in contenuCommande:
        if (idUser == (commande["idUtilisateur"])) :
            # print(commande["tableauDeVente"])
            listeIdVente=(commande["tableauDeVente"])
            for i in listeIdVente:
                # print(i)
                idVente.append(i)
                # print(idVente)
            # print(contenuVente)
            print("{:.^75}".format("Les détails de votre commande sont:"))
            detail,listeIdProduit=getVenteByCommande(listeIdVente,contenuVente)
            listeLibelleP=getProduitByVente(listeIdProduit,contenuProduit)
            print(detail)
            print(listeLibelleP)
            descriptionV=fusionListTupleEtListe(detail,listeLibelleP)
            print(len(descriptionV))
            writeTable(descriptionV,head1)


def saisiCatalogue()->dict:
    print("{:.^50}".format("Saisie du catalogue"))
    nomCatalogue=input("Entrer le nom du catalogue:\n")
    while True:
        try:
            nbreProduit=int(input("Entrer le nbre de produit(s) du catalogue:\n"))
            break
        except ValueError:
            print("Vous avez saisie un caracteur!")
    # print("")
    catalogue= {
            "nom": nomCatalogue,
            "produits": []
        },
    for i in range(nbreProduit):
        print(f"Produits N°{i+1}:\n")
        produit=saisiProduit()
        print(catalogue)
        catalogue[0]["produits"].append(produit)
    return catalogue
# print(saisiCatalogue())
# print(saisiCatalogue())
def createCatalogue():
    db=readOnly(file)
    # print(db[0])
    allData=(db[0])
    s=saisiCatalogue()
    # new=s
    allData["catalogue1"]=dict(s)
    writeOnly(file,allData)
    # json.dump(s,l,indent=4)
    # print(allData)

# createCatalogue()

def afficheProduitOfCatalogue(nom):
    listeP=[]
    db=readOnly(file)
    # print(db[0]["catalogue1"])
    # print(db[0].get("catalogue1"))
    nomTable=(db[0].get(nom))
    # print(nomTable)
    if (not(nomTable)):
        print("Ce catalogue n'existe pas")
    else:
        # print("le catalogue existe")
        pdt_of_table=nomTable.get("produits")
        # print(pdt_of_table)
        for i in pdt_of_table:
            # print(i)
            # print(i.get("libelle"))
            listeP.append((i.get("libelle")))
        # print(s[0].get("libelle"))
        # print(listeP)
        if(not(listeP)):
            print("Le catalogue ne contient pas de produits pour le moment")
        else:
            print("{:.^75}".format("La liste de(s) Produit(s) du catalogue est:"))
            for i,item in enumerate(listeP,1):
                print(f"{i}.{item}")

# afficheProduitOfCatalogue("catalogue1")

def trierProduit(catalogue_a_trier:str)->None:
    tb_a_trier=[]
    db=readOnly(file)
    parti_A_Trier=db[0][catalogue_a_trier]["produits"]
    # print(parti_A_Trier)
    for i in parti_A_Trier:
        # print(i["categorie"]["libelle"])
        tb_a_trier.append((i["categorie"]["libelle"]))
    # print(tb_a_trier)
    listeTrier=sorted(tb_a_trier)
    # print(listeTrier)
    print("Produits trier par catégorie:\n")
    for index in range(len(listeTrier)):
        # print(listeTrier[index])
        for i in parti_A_Trier:
            # print(i["categorie"]["libelle"])
            if(listeTrier[index] == i["categorie"]["libelle"]):
                print(i)


def afficheProduitByCategorie(nomCategorie,nomCatalogue):
    listeP=[]
    db=readOnly(file)
    nomTable=(db[0].get("categorie"))
    # print(nomTable)
    if (not(nomTable)):
        print("Cette categorie n'existe pas\n")
    else:
        for i in nomTable:
            if (i["libelle"] == nomCategorie):
                listeP.append(i["libelle"])
        # print(listeP)
        if (not(listeP)):
            print("Ce produit n'existe pas\n")
        else:
            print("Produit de la catégorie {}".format(i["libelle"]))
            produits=db[0][nomCatalogue]["produits"]
            for i in produits:
                if(i["categorie"]["libelle"] in listeP):
                    print("- {}".format(i["libelle"]))



def mettre_a_JourProduit(catalogue, produit_id, **kwargs):
    for produit in catalogue["produits"]:
        if produit["produit_id"] == produit_id:
            for key, value in kwargs.items():
                produit[key] = value



def mettre_a_jour_prix(nouveauValeur, key, cle,id):
    data = readOnly(file)
    # print(data[0].keys())
    attribut=data[0].keys()
    contenu=data[0]
    if(cle not in attribut ):
        print("la cle n'existe pas !!!")
    else:
        # print(contenu[cle])
        table=contenu[cle]
        tableKeys=contenu[cle][0].keys()
        # print(table,tableKeys)
        if (key not in tableKeys):
            print("la key n'existe pas !!!")
        else:
            for i in table:
                print(i)
                if (i["id"] == id):
                    i[key]=nouveauValeur

    import json

def mettre_a_Jour(nouvelle_valeur, cle_produit, attribut, id_produit, nom_fichier):
    data = readOnly(file)  
    if cle_produit not in data[0]:
        print("La clé spécifiée n'existe pas.")
    produits = data[0][cle_produit]
    if not produits:
        print("La liste des produits est vide.")
    if attribut not in produits[0]:
        print("L'attribut spécifié n'existe pas dans les produits.")
    for produit in produits:
        if produit.get('id') == id_produit:
            produit[attribut] = nouvelle_valeur
            print("Produit mis à jour avec succès :", produit)
            break
    else:
        print("Aucun produit trouvé avec l'ID spécifié.")

    with open(nom_fichier, 'w') as f:
        json.dump(data, f, indent=4)


def etat_caisse_par_date(date, nom_fichier):
    with open(nom_fichier, 'r') as f:
        data = json.load(f)
    
    total_ventes = 0
    print(catalogue)
    for catalogue in data:
        if 'ventes' in catalogue:
            for vente in catalogue['ventes']:
                if vente.get('date') == date:
                    total_ventes += vente.get('prixDeVente') * vente.get('quantiteVendu')
    
    return total_ventes

