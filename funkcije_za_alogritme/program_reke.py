def odpri_datoteko(ime_datoteke):
    with open(ime_datoteke, 'r') as datoteka:
        return datoteka.readlines()

def informacije_reka(ime_datoteke):
    try:
        with open(ime_datoteke, 'r') as datoteka:
            zadnja_vrstica = datoteka.readlines()[-1].strip()
            datum_cas, vodostaj, pretok, temperatura = zadnja_vrstica.split(",")
            print("Datum in čas: {:<1}".format(datum_cas))
            print("Vodostaj: {:<1} cm".format(vodostaj))
            print("Pretok: {:<1} m³/s".format(pretok))
            print("Temperatura: {:<1} °C".format(temperatura))
    except FileNotFoundError:
        print("Datoteka '{}' ne obstaja.".format(ime_datoteke))
    except Exception as e:
        print("Napaka:", e)

def poplavilo(ime_datoteke, max_vodostaj):
    zadnja_vrstica = odpri_datoteko(ime_datoteke)[-1].strip()
    _, vodostaj, _, _ = zadnja_vrstica.split(",")
    vodostaj = int(vodostaj)
    if vodostaj > max_vodostaj:
        print(f"Reka je poplavila! Zadnji vodostaj: {vodostaj} cm")
    else:
        print(f"Reka ni poplavila. Zadnji vodostaj: {vodostaj} cm")

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
    return f"Trenuten pretok: {pretok}, {primerjava}"

def vecji_manjsi_enak(ime_datoteke):
    prejsnji_vodostaj = None
    datoteka = odpri_datoteko(ime_datoteke)
    for i, vrstica in enumerate(reversed(datoteka), start=1):
        element = vrstica.split(",")
        vodostaj = int(element[1])
        if prejsnji_vodostaj is None:
            primerjava = "Prva meritve, ni primerjave"
        elif vodostaj > prejsnji_vodostaj:
            primerjava = "reka narašča!"
        elif vodostaj < prejsnji_vodostaj:
            primerjava = "reka se spušča"
        else:
            primerjava = "enaka kot prejšnja"
        prejsnji_vodostaj = vodostaj  # Shranimo trenutni vodostaj za naslednjo iteracijo

def main():
    ime_datoteke = "/Users/lukarizman/PycharmProjects/TestiranjeKode/example7.csv"
    max_vodostaj = 100  # Nastavite maksimalni vodostaj
    informacije_reka(ime_datoteke)
    poplavilo(ime_datoteke, max_vodostaj)
    print(hitrost_pretok(ime_datoteke))
    vecji_manjsi_enak(ime_datoteke)

if __name__ == "__main__":
    main()
