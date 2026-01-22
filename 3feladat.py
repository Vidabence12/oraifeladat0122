szam = int(input("Adj meg egy számot: "))

osszeg = 0

while szam > 0:
    osszeg = osszeg + (szam % 10)
    szam = szam // 10

print("A számjegyek összege:", osszeg)