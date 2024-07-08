def afficher_menu():
    print("\nChoisissez parmi les 5 options suivantes:")
    print("1- Ajouter un article dans le panier")
    print("2- Supprimer un article du panier")
    print("3- Afficher tous les articles")
    print("4- Vider le panier")
    print("5- Quitter")
    return input("Quel est votre choix? ")

def ajouter_article(panier):
    nom = input("Entrez le nom de l'article: ")
    prix = float(input("Entrez le prix de l'article: "))
    article = {"name": nom, "price": prix}
    panier.append(article)
    print(f"Article {nom} ajouté avec succès.")

def supprimer_article(panier):
    nom = input("Entrez le nom de l'article à supprimer: ")
    for article in panier:
        if article["name"] == nom:
            panier.remove(article)
            print(f"Article {nom} supprimé avec succès.")
            return
    print(f"Aucun article avec le nom {nom} trouvé.")

def afficher_articles(panier):
    if not panier:
        print("Le panier est vide.")
    else:
        for article in panier:
            print(f"Article: {article['name']}, Prix: {article['price']}")

def vider_panier(panier):
    panier.clear()
    print("Le panier a été vidé.")

def main():
    panier = []
    while True:
        choix = afficher_menu()
        if choix == "1":
            ajouter_article(panier)
        elif choix == "2":
            supprimer_article(panier)
        elif choix == "3":
            afficher_articles(panier)
        elif choix == "4":
            vider_panier(panier)
        elif choix == "5":
            print("Fin du programme")
            break
        else:
            print("Choix non valide, veuillez réessayer.")

if __name__ == "__main__":
    main()
