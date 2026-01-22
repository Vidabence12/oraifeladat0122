import random

lista = []
for i in range(10):
    lista.append(random.randint(0, 9))

print("A lista:", lista)

paratlan_db = 0
for szam in lista:
    if szam % 2 == 1:
        paratlan_db += 1

print("Páratlan számok száma:", paratlan_db)

uj_lista = []
for szam in lista:
    if szam not in uj_lista:
        uj_lista.append(szam)

print("Ismétlődések nélkül:", uj_lista)

hianyzo = []
for i in range(10):
    if i not in lista:
        hianyzo.append(i)

if len(hianyzo) == 0:
    print("Minden szám szerepel 0 és 9 között.")
else:
    print("Hiányzó számok:", hianyzo)