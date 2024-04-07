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


informacije_reka("/Users/lukarizman/PycharmProjects/TestiranjeKode/example7.csv")
