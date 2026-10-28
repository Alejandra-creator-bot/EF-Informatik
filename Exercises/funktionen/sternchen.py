def stern5(Breite2):
    print("*"*Breite2)

def stern2(Breite3):
    print(f"{'*':<{Breite3}}*")

def stern(Breite1, Höhe):
    stern5(Breite1)
    for i in range(Höhe):
        stern2(Breite1-1)
    stern5(Breite1)

stern(abs(-5),abs(4))
