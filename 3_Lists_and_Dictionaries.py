# nous allons mettre en place  un programme qui va afficher à l'utilisateur un menu défini en amont pour un panier numérique

# nous allons commencer en mettant en place une fonction qui affiche les differents menu
def afficher_menu():
    print("Choisissez parmi les 5 options suivantes:")
    print("1- Ajouter un article dans le panier")
    print("2- Supprimer un article du panier")
    print("3- Afficher tous les articles")
    print("4- Vider le panier")
    print("5- Quitter")
    return input("Quel est votre choix? ")
# nous allons ensuite creer une fonction qui affichera l'article en fonction de son nom et de son prix
# pour cela il faut ajouter l'option float pour qu'on puisse inserer des décimales 
def ajouter_article(panier):
    nom = input("Entrez le nom de l'article: ")
    prix = float(input("Entrez le prix de l'article: "))
    article = {"name": nom, "price": prix}
    panier.append(article)
    print(f"Article {nom} ajouté avec succès.")
# cette fonction nous permettra de supprimer un article du panier si on le souhaite
def supprimer_article(panier):
    nom = input("Entrez le nom de l'article à supprimer: ")
    for article in panier:
        if article["name"] == nom:
            panier.remove(article)
            print(f"Article {nom} supprimé avec succès.")
            return
    print("Aucun article avec ce nom.")
# cette fonction nous servira a afficher les articles disponibles dans le panier, et à nous signifier qu'il est vide en cas d'abscence d'article
def afficher_articles(panier):
    if not panier:
        print("Le panier est vide.")
    else:
        for article in panier:
            print(f"Article: {article['name']}, Prix: {article['price']}")
# cette fonction nous permettra de vider notre panier 
def vider_panier(panier):
    panier.clear()
    print("Le panier a été vidé.")
# enfin cette fonction nous servira à lancer notre programme 
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
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()