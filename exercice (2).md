A RENDRE : DATE LIMITE VENDREDI 23 A 14H
METTRE LES DEUX FICHIERS (module.py et la documentation .pdf) dans un dossier compressé portant votre nom et votre classe dans le lien suivant: https://www.dropbox.com/request/kzEBxOlh8YRAMKTjl0qQ
EXERCICE 1
Un produit est caracterisé :
    - libelle
    - prix
    - quantite
    - categorie
    - date de peremption
    - id

Une categorie est caracterisée par :
    - libelle
    - id
Un catalogue est caracterisé  par:
    - son nom
    - ses produits

Un utilisateur est caracterisé par:
    - id
    - nom
    - prenom
    - email
    - mot de passe

Une vente est caracterisée par :
    - id
    - idProduit
    - qunatite vendu
    - prix de vente

Une commande est caracterisee par :
    - id
    - tableau de vente
    - date
    - idUtilisateur


Un produit peut etre dans plusieurs categories
Dans une categorie on peut avoir plusieurs produits
Un produit peut ne pas avoir de date de peremption
Une commande peut avoir plusieurs ventes
Une commande est effectuee par un seul utilisateur
Un produit peut etre dans plusieur ventes

QUESTIONS :
    proposer les fonctionnalites suivantes:
    - Se connecter (stocker l'utilisateur connecté dans le fichier json)
    - Se deconnecter 
    - Ajout de nouveau produit au catalogue
    - Creer une vente
    - Effectuer une commande
    - Afficher les details d'une commande (avec le montant total)
    - Ajouter un catalogue
    - Afficher les produits d'un catalogue donné
    - Trier les produit par categorie
    - Afficher les produit d'une categorie donnée
    - Mettre a jour un produit.
    - Avoir L'etat de la caisse par date
NB:
Dans cette exercice vous devez rendre un seul fichier nommé module.py avec toutes les fonctions
Faire toutes les fonctions necessaires pour repondre a ces question (dans une module)
Vous utiliser le module JSON de python (json.dump et json.load)

EXERCICE 2:
Faire un document de presentation de tinyDB avec des exemple : de l'installation a l'utilisation avec des exemple de code. (s'inspirer de OpenClassroom). Le document doit etre complet, propre, bien joli avec des pages numerotés.

DATE LIMITE VENDREDI 14H
