mondat = "A programozás logikus gondolkodást fejleszt"

szavak = mondat.split()

hosszak = []

for szo in szavak:
    hosszak.append(len(szo))

print(hosszak)