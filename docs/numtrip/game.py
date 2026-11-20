board = [
[1, 2, 3, 4, 5,],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]
]
# randint für Anfang? zu jedem Kästchen? Aufpassen nicht bei jedem Ablauf, nur am Anfang. Oder beim Runterfallen.
# Oder randint auch nach dem Klicken? Nur Kästchen auf dem man Draufgecklickt hat 2 mal x.
# Alle die gleiche Zahl wie Kästchen, Zahl ändern. Achtung: müssen das Kästchen berühren!! wie machen?
# Die Kästchen die runterfallen, nicht neu, übernehmen die Zahlen von den Zahlen von den kästchen oberhalb.

def whole_board():
    print("-"*31)
    print(f"¦{board[0][0]:^5}¦{board[0][1]:^5}¦{board[0][2]:^5}¦{board[0][3]:^5}¦{board[0][4]:^5}¦")
    print("-"*31)
    print(f"¦{board[1][0]:^5}¦{board[1][1]:^5}¦{board[1][2]:^5}¦{board[1][3]:^5}¦{board[1][4]:^5}¦")
    print("-"*31)
    print(f"¦{board[2][0]:^5}¦{board[2][1]:^5}¦{board[2][2]:^5}¦{board[2][3]:^5}¦{board[2][4]:^5}¦")
    print("-"*31)
    print(f"¦{board[3][0]:^5}¦{board[3][1]:^5}¦{board[3][2]:^5}¦{board[3][3]:^5}¦{board[3][4]:^5}¦")
    print("-"*31)
    print(f"¦{board[4][0]:^5}¦{board[4][1]:^5}¦{board[4][2]:^5}¦{board[4][3]:^5}¦{board[4][4]:^5}¦")
    print("-"*31)
          
whole_board()


while True:
    y_achse= int(input("Gib eine Zahl von 0-4 ein: "))
    if y_achse == 5:
            break
    x_achse= int(input("Gibt eine Zahl von 0-4 ein: "))
    

    board[y_achse][x_achse]= " "

    whole_board()
    
