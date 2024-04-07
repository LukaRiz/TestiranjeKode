from datetime import datetime, timedelta

def odpri_datoteko(ime_datoteke):
    with open(ime_datoteke, 'r') as datoteka:
        return datoteka.readlines()

def urni_interval(ime_datoteke):
    datoteka = odpri_datoteko(ime_datoteke)
    prejsnji_cas = None
    skupno_ur = 0

    for vrstica in reversed(datoteka):
        datum_cas, _, _, _ = vrstica.split(",")
        _, cas = datum_cas.split(" ")
        trenutni_cas = datetime.strptime(datum_cas, "%d.%m.%Y %H:%M")

        if prejsnji_cas is not None:
            casovna_razlika = trenutni_cas - prejsnji_cas
            skupno_ur += casovna_razlika.total_seconds() / 3600

            # Izpis polne ure
            if int(skupno_ur) > int(skupno_ur - casovna_razlika.total_seconds() / 3600):
                print(f"{int(skupno_ur)} ura")

        prejsnji_cas = trenutni_cas

    return skupno_ur

print(urni_interval("/Users/lukarizman/PycharmProjects/TestiranjeKode/example7.csv"))
#koncano
