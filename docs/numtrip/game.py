L0= [1, 2, 3, 4, 5,]
L1= [6, 7, 8, 9, 10]
L2= [11, 12, 13, 14, 15]
L3= [16, 17, 18, 19, 20]
L4= [21, 22, 23, 24, 25]

# randint für Anfang? zu jedem Kästchen? Aufpassen nicht bei jedem Ablauf, nur am Anfang. Oder beim Runterfallen.
# Oder randint auch nach dem Klicken? Nur Kästchen auf dem man Draufgecklickt hat 2 mal x.
# Alle die gleiche Zahl wie Kästchen, Zahl ändern. Achtung: müssen das Kästchen berühren!! wie machen?
# Die Kästchen die runterfallen, nicht neu, übernehmen die Zahlen von den Zahlen von den kästchen oberhalb.

def Spielfeld():
    print("-"*31)
    print(f"¦{L0[0]:^5}¦{L0[1]:^5}¦{L0[2]:^5}¦{L0[3]:^5}¦{L0[4]:^5}¦")
    print("-"*31)
    print(f"¦{L1[0]:^5}¦{L1[1]:^5}¦{L1[2]:^5}¦{L1[3]:^5}¦{L1[4]:^5}¦")
    print("-"*31)
    print(f"¦{L2[0]:^5}¦{L2[1]:^5}¦{L2[2]:^5}¦{L2[3]:^5}¦{L2[4]:^5}¦")
    print("-"*31)
    print(f"¦{L3[0]:^5}¦{L3[1]:^5}¦{L3[2]:^5}¦{L3[3]:^5}¦{L3[4]:^5}¦")
    print("-"*31)
    print(f"¦{L4[0]:^5}¦{L4[1]:^5}¦{L4[2]:^5}¦{L4[3]:^5}¦{L4[4]:^5}¦")
    print("-"*31)
          
Spielfeld()
