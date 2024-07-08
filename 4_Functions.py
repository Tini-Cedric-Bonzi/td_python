# Programme avec fonctions

def afficher_menu():
    print("\nChoisissez parmi les 5 options suivantes:")
    print("1- Ajouter un article dans le panier")
    print("2- Supprimer un article du panier")
    print("3- Afficher tous les articles")
    print("4- Vider le panier")
    print("5- Quitter")

def ajouter_article(panier):
    article = input("Entrez le nom de l'article: ")
    prix = input("Entrez le prix de l'article: ")
    panier.append({'name': article, 'price': prix})

def supprimer_article(panier):
    article = input("Entrez le nom de l'article à supprimer: ")
    found = False
    for item in panier:
        if item['name'] == article:
            panier.remove(item)
            found = True
            break
    if not found:
        print("Aucun article avec ce nom")

def afficher_articles(panier):
    if not panier:
        print("Le panier est vide")
    for item in panier:
        print(f"Article: {item['name']}, Prix: {item['price']}")

def vider_panier(panier):
    panier.clear()
    print("Le panier a été vidé")

def main():
    panier = []

    while True:
        afficher_menu()
        choix = input("Quel est votre choix? ")

        if choix == '1':
            ajouter_article(panier)
        
        elif choix == '2':
            supprimer_article(panier)

        elif choix == '3':
            afficher_articles(panier)
        
        elif choix == '4':
            vider_panier(panier)

        elif choix == '5':
            print("Fin du programme")
            break

        else:
            print("Choix invalide, veuillez réessayer")

if __name__ == "__main__":
    main()