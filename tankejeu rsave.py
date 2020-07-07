''' jeu tank voila lol'''

'''32tiles tank compris'''
import os
import time
import keyboard

tileg = 15
tiled = 15
tank = "o"
vide = None
sens = False
vitesse = 0.3
tankaaaa = None
tanknb = True
# \CLEAR() / :
# >>>1.Efface toutes les valeurs présentes à l'écran.
def clear():
    os.system('cd C:\\Windows|cls' if os.name == 'nt' else 'clear')


def mouv():
    global tileg, tiled, tank, aa, tilemax, tankaaaa, tanknb, tanke
    tilemax = tiled + tileg
    if sens == False:
        if aa == "g":
            if tiled < tilemax:
                tileg -= 1
                tiled +=1
                jeu()
            else:
                jeu()
        elif aa == "d":
            if tileg < tilemax:
                tileg += 1
                tiled -= 1
                jeu()
            else:
                jeu()
    elif sens == True:
        if aa == "g":
            if tiled < tilemax:
                print("caca")
                tanke = tankaaaa
                tileg -= 1
                tiled += 1
                jeu()
            else:
                jeu()
        elif aa == "d":
            if tileg < tilemax:
                tanke = tank
                tanknb = True
                tileg += 1
                tiled -= 1
                jeu()
            else:
                jeu()


def admin():
    clear()
    global tank, nouveautank, questiontank,nouveautile,questiontile,tiled,tileg,total,vitesse, nouveauvitesse, questionvitesse, sens, tankaaaa

    admine = input("\nCommande administrateur : Que désirez vous faire ? "
                   "\n 1:Changer la valeur du tank ({})"
                   "\n 2:Changer les valeurs des tiles ({}) "
                   "\n 3:Retourner au jeu"
                   "\n 4:Changer la vitesse ({})"
                   "\n 5:Changement de sens ({})".format(tank, total, vitesse, sens))

    if admine == "1":
        nouveautank = input("Veuillez insérer la nouvelle valeur.")
        if nouveautank == tank:
            print("La nouvelle valeur est la même que l'ancienne.")
            time.sleep(2)
            admin()
        else:
            questiontank = input("Etes vous sûr de changer de {} à {} ? (y/n)".format(tank, nouveautank))
            if questiontank == "y":
                tank = nouveautank
                admin()
            elif questiontank == "n":
                print("Commande annulée, retour à la commande administrateur.")
                time.sleep(2)
                admin()

    elif admine == "2":
        nouveautile = input("Veuillez insérer la nouvelle valeur.")
        if nouveautile == tileg + tiled:
            print("La nouvelle valeur est la même que l'ancienne.")
            time.sleep(2)
            admin()
        try:
            nouveautile = int(nouveautile)
        except ValueError:
            print("La valeur ne peut pas correspondre à des lettres. Utilisez des nombres entiers.")
            time.sleep(0.2)
            print("Retour à la commande administrateur.")
            time.sleep(2)
        else:
            questiontile = input("Etes vous sûr de changer de {} à {} ? (y/n)".format(tiled + tileg, nouveautile))

            if questiontile == "y":
                tiled = nouveautile / 2
                tiled = int(tiled)
                tileg = tiled
                admin()
            elif questiontile == "n":
                print("Commande annulée, retour à la commande administrateur.")
                time.sleep(2)
                admin()
            else:
                print("Erreur, retour à la commande administrateur.")
                time.sleep(2)
                admin()

    elif admine == "3":
        jeu()

    elif admine == "4":
        nouveauvitesse = input("Veuillez insérer la nouvelle valeur.")
        if nouveauvitesse == vitesse:
            print("La nouvelle valeur est la même que l'ancienne.")
            time.sleep(2)
            admin()
        try:
            nouveauvitesse = float(nouveauvitesse)
        except ValueError:
            print("La valeur ne peut pas correspondre à des lettres. Utilisez des nombres (entiers ou non).")
            time.sleep(0.2)
            print("Retour à la commande administrateur.")
            time.sleep(2)
        else:
            questionvitesse = input("Etes vous sûr de changer de {} à {} ? (y/n)".format(vitesse, nouveauvitesse))
            if questionvitesse == "y":
                vitesse = nouveauvitesse
                admin()
            elif questionvitesse == "n":
                print("Commande annulée, retour à la commande administrateur.")
                time.sleep(2)
                admin()
            else:
                print("Erreur, retour à la commande administrateur.")
                time.sleep(2)
                admin()

    elif admine == "5":
        if sens == False:
            sens = True
            admin()
        elif sens == True:
            sens = False
            tankaaaa = tank[::-1]
            admin()


    else:
        print("Erreur de valeur, retour à la commande administrateur.")
        time.sleep(2)
        admin()

tanke = tank
def jeu():
    global tileg, tiled, tank, vide, bool, total, aa, aaa, vitesse, tankaaaa, tanke
    tankaaaa = tank[::-1]
    total = tileg + tiled
    vide = total
    vide -= 24
    vide /= 2
    vide += len(tank)
    vide = int(vide)
    aaa = total + len(tank)
    if aaa > 99:
        bool = False
    else:
        bool = True
    if bool == True:
        time.sleep(vitesse)
        clear()
        print("")
        print("{}{}{}\n{}Gauche : {}, Droite : {}".format(tileg * "_", tanke, tiled * "_", vide * " ", tileg,tiled))
        while True:
            if keyboard.is_pressed("q"):
                aa = "g"
                mouv()
                break
            if keyboard.is_pressed("d"):
                aa = "d"
                mouv()
                break
            if keyboard.is_pressed("h"):
                admin()
                break
    elif bool == False:
        print("Vous ne pouvez pas définir au delà de 99 tiles, veuillez changer la valeur.")
        time.sleep(2)
        admin()


jeu()