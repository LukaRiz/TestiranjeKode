#funkcija odpre datoteko ter tudi sama zapre z stavkom "with open..."
def odpri_datoteko(ime_datoteke):
    with open(ime_datoteke, 'r') as datoteka:
        return datoteka.readlines()

#funkcija pove ali gre vrednost cez max vodostaj ali ne
def poplavilo(ime_datoteke, max_vodostaj):
    datoteka = odpri_datoteko(ime_datoteke)
    for i, vrstica in enumerate(reversed(datoteka), start=1):
        print(vrstica)
        element = vrstica.split(",")
        vodostaj = int(element[1])
        if vodostaj > max_vodostaj:
            print(f"Številka meritve: {i}, Količina vodostaja: {vodostaj}, Ali je šlo čez?: Da")

        else:
            print(f"Številka meritve: {i}, Količina vodostaja: {vodostaj}, Ali je šlo čez?: Ne")


#print(poplavilo("example7.csv", 140))

#koncano
