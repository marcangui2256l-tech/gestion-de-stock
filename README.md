# Gestion de stock d'une épicerie (Python)

Programme en ligne de commande qui permet de suivre le stock d'une épicerie.
Les produits sont organisés avec des **dictionnaires** Python.

Projet réalisé en classe de Terminale (spécialité NSI).

## Fonctionnalités

- Afficher le stock (avec un message quand la quantité est inférieure à 10)
- Ajouter un produit
- Rechercher un produit par son nom
- Réapprovisionner un produit
- Vendre un produit (la vente est refusée si le stock est insuffisant)
- Supprimer un produit
- Calculer la valeur totale du stock

## Lancer le programme

Il faut avoir [Python 3](https://www.python.org/downloads/) installé.

```bash
python gestion_stock.py
```

## Structure des données

La clé du dictionnaire est le code du produit. La valeur est un autre dictionnaire
contenant le nom, le prix et la quantité.

```python
stock = {
    "P001": {"nom": "Pommes", "prix": 2.5, "quantite": 40},
    "P002": {"nom": "Lait", "prix": 1.2, "quantite": 8}
}
```

## Limites et améliorations possibles

- Les données ne sont pas sauvegardées : le stock revient à son état de départ à chaque lancement.
- Si on saisit une lettre à la place d'un nombre, le programme s'arrête avec une erreur.
- Idée d'amélioration : enregistrer le stock dans un fichier.

## Auteur

Angui Koffi
