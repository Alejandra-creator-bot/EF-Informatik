

# Variablen
gesucht = 'test'

gefunden = []
falsch_geraten = []

def eingabe():
    buchstabe = input('Buchstabe? ')
    while not is_valid(buchstabe):
        buchstabe = input('Buchstabe? ')
    return buchstabe.lower()

def is_valid(inp):
    if len(inp) == 1 and inp.isalpha():
        return True
    else:
        return False

def auswerten (inp):
    if inp in gesucht:
        gefunden.append(inp)
    else:
        falsch_geraten.append(inp)

def gewonnen ():
    for buchstabe in gesucht:
        if buchstabe not in gefunden:
            return False
    return True

def play():
    print('Falsche Buchstaben:', falsch_geraten)
    for buchstabe in gesucht:
        if buchstabe in gefunden:
            print(buchstabe, end=' ')
        else:
            print('_', end=' ')
    print('')

def spiel():
    versuche= 0
    while not gewonnen() and versuche < 10:   
        inp = eingabe()
        auswerten(inp)
        play()
        versuche += 1

    if gewonnen():
        print("bravo!")
    else:
        print("du hast verloren")

def fragen():
    frage= input("Nochmals spielen? [y], [n]")
    if frage == "y":
        gefunden.clear()
        falsch_geraten.clear()
        spiel()

spiel()
fragen()