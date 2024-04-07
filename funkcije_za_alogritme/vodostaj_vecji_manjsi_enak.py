#funkcija odpre datoteko ter tudi sama zapre z stavkom "with open..."
def odpri_datoteko(ime_datoteke):
    with open(ime_datoteke, 'r') as datoteka:
        return datoteka.readlines()


#vecji_manjsi_enak bejsikli samo pove ali je trenutni vodostaj visji od prejsnega oz. nizji.
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

        print(f"Številka meritve: {i}, Količina vode: {vodostaj}, {primerjava}")

        prejsnji_vodostaj = vodostaj  # Shranimo trenutni vodostaj za naslednjo iteracijo




#print(vecji_manjsi_enak("example7.csv"))
#koncano
