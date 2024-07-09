# nous allons rediger un programme qui demandera à tout utlisateur d'entrer une note , à la suite de la note entrer il obtiendra une mention #

# nous allons tout d'abord definir une fonction qui permettra à l'utilsateur d'entrer une note entre 0 et 20 y compris des notes decimale #
def mention_note():
    note = float(input("Entrez une note: "))
# nous allons à présent demander à notre programme d'afficher les mentions en fonction des notes recu #
    if note >= 18:
        print("Excellent")
    elif note >= 16:
        print("Très bien")
    elif note >= 14:
        print("Bien")
    elif note >= 12:
        print("Satisfaisant")
    elif note >= 10:
        print("Passable")
    else:
        print("Échec")
# nous allons maintenant lancer le programme à travers notre fonction # 
if __name__ == "__main__":
    mention_note()