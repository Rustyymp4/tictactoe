from operator import xor
coordonnees = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
jeu = {}
    
def creer_dico(dico):
    for coordonnee in coordonnees:
        dico[coordonnee] = " "

def creer_arbre(pere) :
    if pere[2] == 9:
        pere[3][2] += 1
        return "égalité"
    for coordonnee in coordonnees:
        jeu_fils = {}
        creer_dico(jeu_fils)
        if pere[0][coordonnee] != ' ':
            if aligne(coordonnee, pere[0]):
                if pere[2] % 2 == 1:
                    pere[3][1] += 1
                    return "défaite"
                elif pere[2] % 2 == 0:
                    pere [3][0] += 1
                    return "victoire"
        elif pere[0][coordonnee] == ' ':
            for case in coordonnees:
                if case == coordonnee:
                    if pere[2] % 2 == 0:
                        jeu_fils[case] = 'O'
                    else:
                        jeu_fils[case] = 'X'
                else:
                    jeu_fils[case] = pere[0][case]
            fils = [jeu_fils, [], pere[2] + 1, [pere[3][0], pere[3][1], pere[3][2]]]
            pere[1].append(fils)
            creer_arbre(fils)

def update_vde(pere):
    for fils in pere[1]:
        update_vde(fils)
        pere[3][0] += fils[3][0]
        pere[3][1] += fils[3][1]
        pere[3][2] += fils[3][2]

def aligne(case, dico):
    ligne = 0
    colonne = 0
    diagonale = 0
    for coordonnee in coordonnees:
        if coordonnee != case:
            if dico [coordonnee] != " " :
                if coordonnee[0] == case[0]:
                    if dico[coordonnee] == dico[case]:
                        colonne +=1
                if coordonnee[1] == case[1]:
                    if dico[coordonnee] == dico[case]:
                        ligne += 1
                if (case[0] == case[1] and coordonnee[0] == coordonnee[1]) or (case[0] == 2 - case[1] and coordonnee[0] == 2 - coordonnee[1]):
                    if dico[coordonnee] == dico[case]:
                        diagonale += 1
    if ligne == 2 or colonne == 2 or diagonale == 2:
        return True
    return False


def choix_bot(plateau, tour):
    ratio = -float("inf")
    arbre = [plateau, [], tour, [0, 0, 0]]
    creer_arbre(arbre)
    update_vde(arbre)
    for fils in arbre[1]:
        victoire = fils[3][0]
        defaite = fils[3][1]
        egalite = fils[3][2]
        if ratio < (victoire + egalite) / (victoire + egalite + defaite):
            ratio = (victoire + egalite) / (victoire + egalite + defaite)
            choix = fils[0]
    for coordonnee in coordonnees:
        if choix[coordonnee] != jeu[coordonnee]:
            return coordonnee

def morpion():
    victoire = False
    egalite = False
    tour = -1
    error = 0
    while not victoire and not egalite:
        tour += 1
        if tour % 2 == 0:
            j1 = input("Choisis un duo de coordonnées (x, y) : ")
            if j1 == "(t, t, n)":
                print(" ", "T", "|", "E", '|', "S", "\n", "-----------", "\n", "", "T", "|", "R", "|", "O", "\n", "-----------", "\n", "", "N", "|", "U", "|", "L")
                victoire = True
            elif j1 == "/win":
                j1 = input("Quel est le code secret?")
                if j1 == "42069":
                    print(" ", "O", "|", "O", '|', "O", "\n", "-----------", "\n", "", "O", "|", "O", "|", "O", "\n", "-----------", "\n", "", "O", "|", "O", "|", "O")
                    tour = 69
                    victoire = True
                else :
                    print("ok tricheur")
                    tour = 0
                    victoire = True
            else:
                try : j1 = (int(j1[1]), int(j1[4]))
                except : None
                while (j1 not in coordonnees or jeu[j1] != " ") and not victoire:
                    if error < 10:
                        error += 1
                        j1 = input("Choisis un duo de coordonnées (x, y) valide STP. ")
                        try : j1 = (int(j1[1]), int(j1[4]))
                        except : None
                    else:
                        victoire = True
                        print("Ru commences à me courir sur le haricot, prends ta win")
                if not victoire:
                    jeu[j1] = "O"
                    victoire = aligne(j1, jeu)
                
        else:
            jeu_actuel = {}
            creer_dico(jeu_actuel)
            for coordonnee in coordonnees:
                jeu_actuel[coordonnee] = jeu[coordonnee]
            bot = choix_bot(jeu_actuel, tour)
            jeu[bot] = "X"
            victoire = aligne(bot, jeu)
            print("Au tour de l'IA!")
            print(" ", jeu[(0, 2)], "|", jeu[(1, 2)], '|', jeu[(2, 2)], "\n", "-----------", "\n", "", jeu[(0, 1)], "|", jeu[(1, 1)], "|", jeu[(2, 1)], "\n", "-----------", "\n", "", jeu[(0, 0)], "|", jeu[(1, 0)], "|", jeu[(2, 0)])
        if tour == 8:
            print("C'est une égalité ! Domaj") 
            egalite = True
    if victoire :
        if tour == 69:
            print("Bah gg mon reuf")
        elif tour == 0:
            print("gg tu as loose ezzz")
        elif tour % 2 == 0:
            print("Tu as gagné ! Trop fort mec")
        else:
            print("Tu as perdu ! große Scheiße")


creer_dico(jeu)
morpion()