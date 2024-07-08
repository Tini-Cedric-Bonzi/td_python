# Nous allons mettre en place  un programme qui affiche les 10 premiers nombres pairs en utilisant une boucle For#
#Ensuite, nous allons utiliser une boucle while pour afficher les 10 premiers nombres#
print("Les 10 premiers nombres pairs sont :")
for i in range(1, 11):
    print(i * 2)


print("\nLes 10 premiers nombres impairs sont :")
j = 1
count = 0
while count < 10:
    print(j)
    j += 2
    count += 1

    # Fonction pour demander un nombre à l'utilisateur et vérifier qu'il s'agit bien d'un nombre entier
def demander_nombre():
    while True:
        try:
            nombre = int(input("Veuillez entrer un nombre entier: "))
            return nombre
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

# Demander le nombre à l'utilisateur
nombre_utilisateur = demander_nombre()

# Afficher les nombres entiers entre 1 et le nombre fourni par l'utilisateur en utilisant une boucle For
print("Affichage avec boucle For :")
for i in range(1, nombre_utilisateur + 1):
    print(i, end=" ")

# Afficher les nombres entiers entre 1 et le nombre fourni par l'utilisateur en utilisant une boucle While
print("\n\nAffichage avec boucle While :")
i = 1
while i <= nombre_utilisateur:
    print(i, end=" ")
    i += 1


