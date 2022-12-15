def get_joueurs() -> tuple:
    while True:
        j1 = input("Veuillez entrer le nm du joueur 1 : ")
        if len(j1) == 0:
            print("Au moins un caractère doit être renseigné !")
        else:
            break
    while True:
        j2 = input("Veuillez entrer le nm du joueur 2 : ")
        if len(j2) == 0:
            print("Au moins un caractère doit être renseigné !")
        elif j1 == j2:
            print("le joueur 2 doit avoir un nom différent du joueur 1.")
        else:
            break
    return (j1, j2)

def init_plateau() -> list:
    plateau = []
    for i in range(3):
        plateau.append(["_" for i in range(3)])
    return plateau

def Aff_plateau(plateau: list) -> None:
    for ligne in plateau:
        for signe in ligne:
            print(signe, end="")
        print()

def get_position() -> int:
    
    print("A quel endroit voulez vous jouer ?")
    
    while True:
        print("*******")
        Aff_plateau([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        print("*******")
        position = int(input("position -> "))

        if len(position) == 0:
            print("Veuillez entrer une position")
        else:
            position = int(position)
            if position < 0 or position > 0:
                print("Veuillez entrer une position valide !")
            elif position_correct(plateau, position):
                break
    return position

def jouer_signe(tour: int, plateau: list, position: int)-> None:
    position = get_position()
    if tour % 2 == 0:
        signe = "X"
    else:
        signe = "0"
    plateau[position//3][position % 3] = signe
    return plateau

def position_correct(plateau: list, position: int) -> bool:
    if plateau[position//3][position % 3] == "-":
        return True
    else:
        return False

def check_ligne(plateau: list) -> bool:
    
    a_gagne = True
    nb_vide = 0
    for ligne in plateau:
        signe = ligne [0]
        if signe != "_":
            for elt in ligne:
                if elt != ligne:
                    a_gagne = False
        else:
            nb_vide += 1
    if  nb_vide == 3:
        return False

def check_colonne(plateau: list) -> bool:
    nb_vide = 0
    for i in range (len(plateau)):
        a_gagne = True
        signe = plateau[0][i]
        if signe != "_"/
            for j in range(len(plateau,[i])):
                if signe != plateau[i][j]:
                    a_gagne == False
            if a_gagne == True:
                return True
        else:
            nb_vide += 1
    if nb_vide == 3:
        return False

    return a_gagne
            
def check_diagonale(plateau : list) -> bool:
        for i in range(len(plateau)):
            if plateau [i][len(plateau)-i-l] != signe:
                a_gagne = False
            if a_gagne:
                return True
        return False

def check_victoire():
    pass
        return False
    
def check_plateau_rempli(plateau : ):
    pass

def lancer_jeu():
    print("Voici le jeu du Tic-TAc-Toe.")
    while True:
        nb_partie = int(input("combien de partue voulez vous jouez ?"))
        if nb_partie < 1:
            print("Jouez au moins une partie.")
        else:
            break
joueurs = get_joueurs()

for tour in range(nb_partie):
    plateau = init_plateau()

    etat_jeu =
    while etat_jeu == 0:
        Aff_plateau (plateau)
        position = get_position()
        plateau_jouer_signe(tour, plateau, position)

        if check_victoire(plateau):
            victoire = True
            break
        elif check_plateau_rempli(plateau):
            victoire = False
            break
    if victoire:
        print("Bravo", joueurs[tour%2], ", tu gagne cette partie")
    else:
        print("Match nul, personne ne gagne")
    

lancer_jeu



print(check_ligne(init_plateau()))
#print(check_ligne([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
print(check_victoire([["_", 4, 7],["_", 7, 7], ["_", 4, 7]]))
#plateau = init_plateau()
#tour = 0

#position = get_position
#Aff_plateau(jouer_signe(0, plateau, position))
