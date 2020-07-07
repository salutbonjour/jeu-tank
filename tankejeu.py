''' jeu tank voila lol'''

import os
import time
import keyboard

a1a = 15
a1b = 15
a1c = "o"
a1d = None
a1m = False
a1i = 0.3
a1j = None
a1n = True
a1k = a1c


def aaaa():
    os.system('cd C:\\Windows|cls' if os.name == 'nt' else 'clear')


def aaab():
    global a1a, a1b, a1c, a1g, aaab, a1j, a1n, a1k
    aaab = a1b + a1a
    if a1m == False:
        if a1g == "g":
            if a1b < aaab:
                a1a -= 1
                a1b += 1
                aaad()
            else:
                aaad()
        elif a1g == "d":
            if a1a < aaab:
                a1a += 1
                a1b -= 1
                aaad()
            else:
                aaad()
    elif a1m == True:
        if a1g == "g":
            if a1b < aaab:
                a1k = a1j
                a1a -= 1
                a1b += 1
                aaad()
            else:
                aaad()
        elif a1g == "d":
            if a1a < aaab:
                a1k = a1c
                a1n = True
                a1a += 1
                a1b -= 1
                aaad()
            else:
                aaad()


def aaac():
    aaaa()
    global a1c, nouveautank, questiontank, nouveautile, questiontile, a1b, a1a, a1f, a1i, nouveauvitesse, questionvitesse, a1m, a1j

    admine = input("\nCommande administrateur : Que désirez vous faire ? "
                   "\n 1:Changer la valeur du tank ({})"
                   "\n 2:Changer les valeurs des tiles ({}) "
                   "\n 3:Retourner au jeu"
                   "\n 4:Changer la vitesse ({})"
                   "\n 5:Changement de sens ({})".format(a1c, a1f, a1i, a1m))

    if admine == "1":
        nouveautank = input("Veuillez insérer la nouvelle valeur.")
        if nouveautank == a1c:
            print("La nouvelle valeur est la même que l'ancienne.")
            time.sleep(2)
            aaac()
        else:
            questiontank = input("Etes vous sûr de changer de {} à {} ? (y/n)".format(a1c, nouveautank))
            if questiontank == "y":
                a1c = nouveautank
                aaac()
            elif questiontank == "n":
                print("Commande annulée, retour à la commande administrateur.")
                time.sleep(2)
                aaac()

    elif admine == "2":
        nouveautile = input("Veuillez insérer la nouvelle valeur.")
        if nouveautile == a1a + a1b:
            print("La nouvelle valeur est la même que l'ancienne.")
            time.sleep(2)
            aaac()
        try:
            nouveautile = int(nouveautile)
        except ValueError:
            print("La valeur ne peut pas correspondre à des lettres. Utilisez des nombres entiers.")
            time.sleep(0.2)
            print("Retour à la commande administrateur.")
            time.sleep(2)
        else:
            questiontile = input("Etes vous sûr de changer de {} à {} ? (y/n)".format(a1b + a1a, nouveautile))

            if questiontile == "y":
                a1b = nouveautile / 2
                a1b = int(a1b)
                a1a = a1b
                aaac()
            elif questiontile == "n":
                print("Commande annulée, retour à la commande administrateur.")
                time.sleep(2)
                aaac()
            else:
                print("Erreur, retour à la commande administrateur.")
                time.sleep(2)
                aaac()

    elif admine == "3":
        aaad()

    elif admine == "4":
        nouveauvitesse = input("Veuillez insérer la nouvelle valeur.")
        if nouveauvitesse == a1i:
            print("La nouvelle valeur est la même que l'ancienne.")
            time.sleep(2)
            aaac()
        try:
            nouveauvitesse = float(nouveauvitesse)
        except ValueError:
            print("La valeur ne peut pas correspondre à des lettres. Utilisez des nombres (entiers ou non).")
            time.sleep(0.2)
            print("Retour à la commande administrateur.")
            time.sleep(2)
        else:
            questionvitesse = input("Etes vous sûr de changer de {} à {} ? (y/n)".format(a1i, nouveauvitesse))
            if questionvitesse == "y":
                a1i = nouveauvitesse
                aaac()
            elif questionvitesse == "n":
                print("Commande annulée, retour à la commande administrateur.")
                time.sleep(2)
                aaac()
            else:
                print("Erreur, retour à la commande administrateur.")
                time.sleep(2)
                aaac()

    elif admine == "5":
        if a1m == False:
            a1m = True
            aaac()
        elif a1m == True:
            a1m = False
            a1j = a1c[::-1]
            aaac()


    else:
        print("Erreur de valeur, retour à la commande administrateur.")
        time.sleep(2)
        aaac()


def aaad():
    global a1a, a1b, a1c, a1d, a1e, a1f, a1g, a1h, a1i, a1j, a1k
    a1j = a1c[::-1]
    a1f = a1a + a1b
    a1d = a1f
    a1d -= 24
    a1d /= 2
    a1d += len(a1c)
    a1d = int(a1d)
    a1h = a1f + len(a1c)
    if a1h > 99:
        a1e = False
    else:
        a1e = True
    if a1e == True:
        time.sleep(a1i)
        aaaa()
        print("")
        print("{}{}{}\n{}Gauche : {}, Droite : {}".format(a1a * "_", a1k, a1b * "_", a1d * " ", a1a, a1b))
        while True:
            if keyboard.is_pressed("q"):
                a1g = "g"
                aaab()
                break
            if keyboard.is_pressed("d"):
                a1g = "d"
                aaab()
                break
            if keyboard.is_pressed("h"):
                aaac()
                break
    elif a1e == False:
        print("Vous ne pouvez pas définir au delà de 99 tiles, veuillez changer la valeur.")
        time.sleep(2)
        aaac()


def start():
    aaad()


start()
