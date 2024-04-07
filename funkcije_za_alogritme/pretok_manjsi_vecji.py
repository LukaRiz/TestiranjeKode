def odpri_datoteko(ime_datoteke):
    with open(ime_datoteke, 'r') as datoteka:
        return datoteka.readlines()


def hitrost_pretok(ime_datoteke):
    prejsnji_pretok = None
    datoteka = odpri_datoteko(ime_datoteke)
    for vrstica in reversed(datoteka):
        podatki = vrstica.strip().split(",")
        _, _, pretok, _ = podatki
        primerjava = ""
        if prejsnji_pretok is None:
            primerjava = "Prva meritev, ni primerjave"
        elif float(pretok) > float(prejsnji_pretok):
            primerjava = "Pretok narašča!"
        elif float(pretok) < float(prejsnji_pretok):
            primerjava = "Pretok se spušča!"
        else:
            primerjava = "Pretok enak kot pri prejšnji meritvi"


        prejsnji_pretok = pretok  # Shranimo trenutni pretok za naslednjo iteracijo
    return print(f"Trenuten pretok: {pretok}, {primerjava}")

hitrost_pretok("/Users/lukarizman/PycharmProjects/TestiranjeKode/example7.csv")
#koncano
