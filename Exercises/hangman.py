for buchstabe in gesucht:
    if buchstabe not in gefunden:
        return False
return True

if valid_inp in gesucht:
    gefunden.append(valid_inp)
else:
    falsch_geraten.append(valid_inp)

buchstabe = input('Buchstabe? ')
while not is_valid(buchstabe):
    buchstabe = input('Buchstabe? ')
return buchstabe.lower()

print('Falsche Buchstaben:', falsch_geraten)
for buchstabe in gesucht:
    if buchstabe in gefunden:
        print(buchstabe, end=' ')
    else:
        print('_', end=' ')
print('')

print('Falsche Buchstaben:', falsch_geraten)
for buchstabe in gesucht:
    if buchstabe in gefunden:
        print(buchstabe, end=' ')
    else:
        print('_', end=' ')
print('')


# Variablen
gesucht = 'test'

gefunden = []
falsch_geraten = []