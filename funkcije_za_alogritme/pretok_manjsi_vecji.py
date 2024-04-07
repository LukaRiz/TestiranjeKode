def odpri_datoteko(ime_datoteke):
    with open(ime_datoteke, 'r') as datoteka:
        return datoteka.readlines()


def hitrost_pretok(ime_datoteke):
    datoteka = odpri_datoteko(ime_datoteke)
    for vrstica in reversed(datoteka):
        podatki = vrstica.strip().split(",")
        _, _, pretok, _ = podatki
        print(pretok, "m3/s")




print(hitrost_pretok("/Users/lukarizman/PycharmProjects/TestiranjeKode/example7.csv"))