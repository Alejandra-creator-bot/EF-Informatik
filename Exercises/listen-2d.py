#Aufgabe 1 Pretty_print
'''
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

zeilen = []

for i in range(ZEILEN):
    spalten = []
    for j in range(SPALTEN):
        spalten.append (ZAHL)
    zeilen.append (spalten)
      
matrix = [(zeilen)]

print(matrix)
'''
#Aufgabe 4

SIZE = int(input("SIZE = "))
matrix1 = []

for i in range(1,SIZE+1):
    spalten = []
    for j in range(1,SIZE+1):
        if j/(i) == 1:
            spalten.append (1)
        else:
            spalten.append (0)
    matrix1.append (spalten)


matrix = [(matrix1)]
print(matrix)

