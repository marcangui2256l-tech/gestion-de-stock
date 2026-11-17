# Gestion de stock d'une épicerie avec des dictionnaires
#
# Structure : la clé est le code du produit, la valeur est un dictionnaire.
#
# stock = {
#     "P001": {"nom": "Pommes", "prix": 2.5, "quantite": 40},
#     "P002": {"nom": "Lait",   "prix": 1.2, "quantite": 8}
# }

SEUIL = 10   # en dessous de cette quantité, le stock est faible

stock = {
    "P001": {"nom": "Pommes", "prix": 2.5, "quantite": 40},
    "P002": {"nom": "Lait", "prix": 1.2, "quantite": 8},
    "P003": {"nom": "Pain", "prix": 1.0, "quantite": 25},
    "P004": {"nom": "Oeufs", "prix": 2.1, "quantite": 5}
}


def ajouter_produit(stock, code, nom, prix, quantite):
    """Ajoute un produit. Renvoie False si le code existe déjà."""
    if code in stock:
        return False
    stock[code] = {"nom": nom, "prix": prix, "quantite": quantite}
    return True


def afficher_stock(stock):
    """Affiche tous les produits."""
    if len(stock) == 0:
        print("Le stock est vide.")
    else:
        for code in stock:
            p = stock[code]
            print(code, "|", p["nom"], "|", p["prix"], "euros |", p["quantite"], "en stock")
            if p["quantite"] < SEUIL:
                print("   -> stock faible !")


def rechercher_produit(stock, nom):
    """Renvoie le code du produit qui a ce nom, ou None s'il n'existe pas."""
    for code in stock:
        if stock[code]["nom"].lower() == nom.lower():
            return code
    return None


def reapprovisionner(stock, code, quantite):
    """Ajoute des unités au stock d'un produit."""
    if code in stock:
        stock[code]["quantite"] = stock[code]["quantite"] + quantite
        return True
    return False


def vendre(stock, code, quantite):
    """Retire des unités du stock. Renvoie le prix total, ou -1 si la vente est impossible."""
    if code not in stock:
        return -1
    if stock[code]["quantite"] < quantite:
        return -1
    stock[code]["quantite"] = stock[code]["quantite"] - quantite
    return quantite * stock[code]["prix"]


def supprimer_produit(stock, code):
    """Supprime un produit du stock."""
    if code in stock:
        del stock[code]
        return True
    return False


def valeur_totale(stock):
    """Calcule la valeur totale du stock : somme de prix x quantité."""
    total = 0
    for code in stock:
        total = total + stock[code]["prix"] * stock[code]["quantite"]
    return total


def menu():
    print()
    print("===== ÉPICERIE : GESTION DU STOCK =====")
    print("1 - Afficher le stock")
    print("2 - Ajouter un produit")
    print("3 - Rechercher un produit")
    print("4 - Réapprovisionner")
    print("5 - Vendre un produit")
    print("6 - Supprimer un produit")
    print("7 - Valeur totale du stock")
    print("0 - Quitter")


# ----- Programme principal -----
choix = ""
while choix != "0":
    menu()
    choix = input("Votre choix : ")

    if choix == "1":
        afficher_stock(stock)

    elif choix == "2":
        code = input("Code du produit : ")
        nom = input("Nom : ")
        prix = float(input("Prix : "))
        quantite = int(input("Quantité : "))
        if ajouter_produit(stock, code, nom, prix, quantite):
            print("Produit ajouté.")
        else:
            print("Ce code existe déjà.")

    elif choix == "3":
        nom = input("Nom du produit : ")
        code = rechercher_produit(stock, nom)
        if code is None:
            print("Produit introuvable.")
        else:
            print(code, stock[code]["nom"], stock[code]["prix"], "euros,", stock[code]["quantite"], "en stock")

    elif choix == "4":
        code = input("Code du produit : ")
        quantite = int(input("Quantité reçue : "))
        if reapprovisionner(stock, code, quantite):
            print("Nouveau stock :", stock[code]["quantite"])
        else:
            print("Code introuvable.")

    elif choix == "5":
        code = input("Code du produit : ")
        quantite = int(input("Quantité vendue : "))
        total = vendre(stock, code, quantite)
        if total == -1:
            print("Vente impossible (code inconnu ou stock insuffisant).")
        else:
            print("Vente enregistrée :", round(total, 2), "euros")

    elif choix == "6":
        code = input("Code du produit : ")
        if supprimer_produit(stock, code):
            print("Produit supprimé.")
        else:
            print("Code introuvable.")

    elif choix == "7":
        print("Valeur totale du stock :", round(valeur_totale(stock), 2), "euros")

    elif choix == "0":
        print("Au revoir !")

    else:
        print("Choix invalide.")
