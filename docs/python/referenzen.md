```py 
matrix = []

zeile = [0, 1, 0]
for i in range(3):
    matrix.append(zeile)

print(matrix)

matrix[1][1] = 0 # nur den Wert in Zeile 1 in der Mitte auf 0 Setzen

print(matrix)
```
- Angegeben ist:
    - `matrix = []`, leer
    - `zeile = [0,1,0]`

- Schleife `for i in range (3):`, wird 3 mal ausgeführt
    - zu `matrix.append(zeile)`, zu `matrix []`, leer `zeile = [0,1,0]` hinzufügen und dies 3 mal.

- `print(matrix)`

- Neu definieren:
    - `matrix [1][1] = 0`, 1. Element ist `matrix = 0` nach der Schleife ist dann matrix = `[[0, 1, 0], [0, 1, 0], [0, 1, 0]]` und matrix besteht aus `zeile`, es hat nur 1 zeile, nicht zeile1, zeile2, zeile3. Weil es also aus `zeile` besteht (nur aus 1 zeile), wenn man es bei irgendeine zeile verändert, wird es bei allen verändert.
    
-`print(matrix)`, neue matrix. 
