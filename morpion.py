# Assigne tab1 en liste a 3 arguments, egaux a 1, 2 et 3
tab1 = ["1", "2", "3"]
# Assigne tab2 en liste a 3 arguments, egaux a 1, 2 et 3
tab2 = ["4", "5", "6"]
# Assigne tab3 en liste a 3 arguments, egaux a 1, 2 et 3
tab3 = ["7", "8", "9"]
# Definir une fonction ticTacToe qui lance la partie
def ticTacToe():
    # On definit le boolean win a false
    win = False
    # Tant que tour n'est pas egal a 9
    for tour in range (1, 10):
        # Si win est egal a True
        if win == True:
            # Faire un break
            break
        # Si win est egal a false
        
        if win == False:
            # Si le modulo 2 de tour n'est pas egal a 0 (Si tour est impaire)
            if tour % 2 != 0:
                # Lancer le tour du joueur 1
                tourJ1()
                # Afficher le tableau
                print (tab1)
                print (tab2)
                print (tab3)
                # Print le tour
                print ("Tour n°", tour)

        # Si win est egal a false
        if win == False:
            # Si le modulo 2 de tour est egal a 0 (Si tour est paire)
            if tour % 2 == 0:   
                # Lancer le tour du joueur 2    
                tourJ2()
                # Afficher le tableau
                print (tab1)
                print (tab2)
                print (tab3)
                # Print le tour
                print ("Tour n°", tour)


        # On note les conditions de victoire de J1 en ligne
        if tab1[0] == tab1[1] == tab1[2] == "X":
            print("Bravo J1! Tu as gangé!!")
            win = True
        if tab2[0] == tab2[1] == tab2[2] == "X":
            print("Bravo J1! Tu as gangé!!")
            win = True
        if tab3[0] == tab3[1] == tab3[2] == "X":
            print("Bravo J1! Tu as gangé!!")
            win = True
        # On note les conditions de victoire de J1 en collone
        if tab1[0] == tab2[0] == tab3[0] == "X":
            print("Bravo J1! Tu as gangé!!")
            win = True
        if tab1[1] == tab2[1] == tab3[1] == "X":
            print("Bravo J1! Tu as gangé!!")
            win = True
        if tab1[2] == tab2[2] == tab3[2] == "X":
            print("Bravo J1! Tu as gangé!!")
            win = True
        # On note les conditions de victoire de J1 en diagonale
        if tab1[0] == tab2[1] == tab3[2] == "X":
            print("Bravo J1! Tu as gangé!!")
            win = True
        if tab1[2] == tab2[1] == tab3[0] == "X":
            print("Bravo J1! Tu as gangé!!")
            win = True

        # On note les conditions de victoire de J2 en ligne
        if tab1[0] == tab1[1] == tab1[2] == "O":
            print("Bravo J2! Tu as gangé!!")
            win = True
        if tab2[0] == tab2[1] == tab2[2] == "O":
            print("Bravo J2! Tu as gangé!!")
            win = True
        if tab3[0] == tab3[1] == tab3[2] == "O":
            print("Bravo J2! Tu as gangé!!")
            win = True
        # On note les conditions de victoire de J2 en collone
        if tab1[0] == tab2[0] == tab3[0] == "O":
            print("Bravo J2! Tu as gangé!!")
            win = True
        if tab1[1] == tab2[1] == tab3[1] == "O":
            print("Bravo J2! Tu as gangé!!")
            win = True
        if tab1[2] == tab2[2] == tab3[2] == "O":
            print("Bravo J2! Tu as gangé!!")
            win = True
        # On note les conditions de victoire de J2 en diagonale
        if tab1[0] == tab2[1] == tab3[2] == "O":
            print("Bravo J2! Tu as gangé!!")
            win = True
        if tab1[2] == tab2[1] == tab3[0] == "O":
            print("Bravo J2! Tu as gangé!!")
            win = True

    #Si aucune condition n'est remplie dans les 9 tours impartis alors print un message d'égalité
    print("égalité gros noob")


# Defini tourJ1
def tourJ1():  
    # Assigne plr1 a un input et remplace la case visée
    plr1 = input("Quelle case choisis-tu ? ")
    if plr1 ==  "1" and tab1[0] not in ["O", "X"]:
        tab1[0] = "X"
    elif plr1 ==  "2" and tab1[1] not in ["O", "X"]:
        tab1[1] = "X"
    elif plr1 ==  "3" and tab1[2] not in ["O", "X"]:
        tab1[2] = "X"
    elif plr1 ==  "4" and tab2[0] not in ["O", "X"]:
        tab2[0] = "X"
    elif plr1 ==  "5" and tab2[1] not in ["O", "X"]:
        tab2[1] = "X"
    elif plr1 ==  "6" and tab2[2] not in ["O", "X"]:
        tab2[2] = "X"
    elif plr1 ==  "7" and tab3[0] not in ["O", "X"]:
        tab3[0] = "X"
    elif plr1 ==  "8" and tab3[1] not in ["O", "X"]:
        tab3[1] = "X"
    elif plr1 ==  "9" and tab3[2] not in ["O", "X"]:
        tab3[2] = "X"
    # Si aucune condtion n'est remplie (valeur incorrecte ou case deja prise)
    else :
        # Print valeur incorrecte
        print("Valeur incorrecte")
        # Relancer le tour
        tourJ1()

# Defini tourJ2
def tourJ2():
    # Assigne plr2 a un input et remplace la case visée
    plr2 = input("Quelle case choisis-tu ? ")
    if plr2 ==  "1" and tab1[0] not in ["O", "X"]:
        tab1[0] = "O"
    elif plr2 ==  "2" and tab1[1] not in ["O", "X"]:
        tab1[1] = "O"
    elif plr2 ==  "3" and tab1[2] not in ["O", "X"]:
        tab1[2] = "O"
    elif plr2 ==  "4" and tab2[0] not in ["O", "X"]:
        tab2[0] = "O"
    elif plr2 ==  "5" and tab2[1] not in ["O", "X"]:
        tab2[1] = "O"
    elif plr2 ==  "6" and tab2[2] not in ["O", "X"]:
        tab2[2] = "O"
    elif plr2 ==  "7" and tab3[0] not in ["O", "X"]:
        tab3[0] = "O"
    elif plr2 ==  "8" and tab3[1] not in ["O", "X"]:
        tab3[1] = "O"
    elif plr2 ==  "9" and tab3[2] not in ["O", "X"]:
        tab3[2] = "O"
    # Si aucune condtion n'est remplie (valeur incorrecte ou case deja prise)
    else :
        # Print valeur incorrecte
        print("Valeur incorrecte")
        # Recommencer l'input
        tourJ2()


ticTacToe()