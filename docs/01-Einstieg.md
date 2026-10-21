# Einstieg

Meine Lösung zu Aufgabe 1:  

```py
z=5

for i in range (1,6):
    if z % (i)== 0:
        print ("!", end=' ')
    else:
        print (".", end=' ')
```

Beachtenswert:
- Die Schleife `for i in range (n)`läuft von 0 bis n-1.
    - Deswegen schreibe ich es soll bei 1 anfangen und bis n+1 gehen, also 6. `(1,6)`
    
- Das zusätzliche `end=` in der `print()` Funktion macht, dass es keinen Zeilenumbruch gibt.
    - `print("hallo")`entspricht eigentlich zu `print("hallo", end="/n")`. Das `/n` in `end=` bewirk einen Zeilenumbruch.
    - Ohne das `/n`gibt es keinen Zeilenumbruch und macht auf der gleichen Zeile weiter. 