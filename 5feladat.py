szamok = []

while True:
    adat = input("szám (stop a vége): ")

    if adat == "stop":
        break

    szam = int(adat)
    szamok.append(szam)

print("számok száma:", len(szamok))

kulonbseg = max(szamok) - min(szamok)
print("legnagyobb és legkisebb különbsége:", kulonbseg)

harommal_oszthato = []

for szam in szamok:
    if szam % 3 == 0:
        harommal_oszthato.append(szam)

print("3mal osztható számok:", harommal_oszthato)