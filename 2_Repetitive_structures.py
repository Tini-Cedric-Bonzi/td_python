#exercice 1: nous allons mettre en place un programme qui nous permettre d'afficher les 10 premiers nombre pairs grace à for 
# dans un deuxième temps nous allons creer une boucle while pour afficher les nombres impaire
print("afficher les 10 premiers nombres pairs")
for i in range (2, 21, 2):
    print(i)

print("afficher les 10 prmiers nombres impairs")
number = 0
count = 0
while count < 10:
    if number  % 2 != 0:
        print(number)
        count += 1
    number += 1

    # exercice 2: nous allons créer un programme qui va demander un nombre à l’utilisateur
    # le programme va s’assurer que c’est bien un nombre qui a été inséré 
    #  à la fin  il va afficher les nombres entier entre le 1 et le nombre fourni par l’utilisateur

# nous allons tout d'abord mettre en place une fonction pour vérifier si l'entrée de l'utilisateur est un nombre
def demander_nombre():
# la fonction while permet de mettre en place une boucle qui prendra fin que lorsque un nombre entier sera inserer
    while True:
# cette étape permettra de convertir l'entrer en entier grace au int, en cas d'échec elle sera conciderer comme une erreur et affichera le message indiquer
        try:
            nombre = int(input("Veuillez entrer un nombre entier: "))
            return nombre
        except ValueError:
            print("Ce n'est pas un nombre entier. Veuillez réessayer.")

# Demander le nombre à l'utilisateur
nombre = demander_nombre()

# Utilisation de la boucle for pour afficher les nombres de 1 à nombre choisis
print("Affichage:")
for i in range(1, nombre + 1):
    print(i) 

