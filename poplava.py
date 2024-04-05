datoteka = open("example1_predelan_za_simulacijo_poplav.csv") #odprem datoteko, ki jo dobi program. Datoteka vsebuje elemente, ki so datum, vodostaj v cm, pretok ter temperatura

random_max_vodostaj_reke = 500
for vrstica in datoteka:
    element = vrstica.split(",") #v csv so loceni podatki z vejicami
    vodostaj = element[1]   #drugi element predstavlja vodostaj
    print(vodostaj)
hhh