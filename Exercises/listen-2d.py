#Aufgabe 1 Pretty_print

def pretty_print(mat2d):
    for row in mat2d:
        print(row)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6]]

pretty_print(matrix)
pretty_print(matrix1)

#Achtung nicht `pretty_print` ([matrix]) schreiben weil sonst [matrix] als 1 Element angeschaut wird!

#Aufgabe 2 

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f'[i: {i}, j: {j}] =', matrix[i][j])

#Aufgabe 3

ZEILEN = int(input("ZEILE = "))
SPALTEN = int(input("SPALTEN = "))
ZAHL = int(input("ZAHL = "))
    
for i in range(ZEILEN):
    zeilen = []
    for j in range(SPALTEN):
        spalten = []
        spalten.append (ZAHL)
    zeilen.append (spalten)
    
'''    
matrix = []

print(matrix)

'''

