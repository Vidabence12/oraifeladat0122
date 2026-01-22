mondat = input("mondat: ")

if mondat.endswith("?"):
    print("kérdő mondat")
elif mondat.endswith("!"):
    print("felszólító vagy óhajtó")
else:
    print("kijelentő")