from datetime import datetime, timedelta

def odpri_datoteko(ime_datoteke):
    with open(ime_datoteke, 'r') as datoteka:
        return datoteka.readlines()


#zacetek funkcije za urni interval za računanje koliko narašča na uro posamezna reka
def urni_interval(ime_datoteke):
    datoteka = odpri_datoteko(ime_datoteke)
    prejsnji_cas = None
    skupno_minut = 0

    for vrstica in reversed(datoteka):
        datum_cas, vodostaj, pretok, temp = vrstica.split(",")
        datum, cas = datum_cas.split(" ")
        print(datum, cas)


print(urni_interval("example7.csv"))