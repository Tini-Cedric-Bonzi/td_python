# nous allons definir un programme qui permettra à un utlisateur de connaitre sa mention en fonction de sa note #
def obtenir_note():
    while True:
        note = input("Veuillez entrer une note (0-20) : ")
        if note.replace('.', '', 1).isdigit():
            note = float(note)
            if 0 <= note <= 20:
                return note
        print("Entrée invalide, veuillez entrer une note entre 0 et 20.")

def afficher_mention(note):
    if note >= 18:
        print("Excellent")
    elif 16 <= note < 18:
        print("Très bien")
    elif 14 <= note < 16:
        print("Bien")
    elif 12 <= note < 14:
        print("Satisfaisant")
    elif 10 <= note < 12:
        print("Passable")
    else:
        print("Échec")

def main():
    note = obtenir_note()
    afficher_mention(note)

if __name__ == "__main__":
    main()

