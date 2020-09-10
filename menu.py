from laul import Laul
from laulja import Laulja
from album import Album
import csv
# Tabeli loomine
tabel = []

with open("albumid", "r+") as f:
    reader = csv.reader(f, delimiter="\t")
    for line in reader:
        tabel.append(line)

print(tabel)

laulud = []
lauljad = []
albumid = []

artist = []
album = []
l1 = []
# võtab välja tabelist laulud, lauljad ja albumid
for line in tabel:
    laulja = Laulja(line[0])
    if line[0] not in artist:
        lauljad.append(laulja)
        artist.append(line[0])
        laulja.albumid.append(line[1])
for line in tabel:
    albumi = Album(line[1], line[0], line[2])
    if line[1] not in album:
        albumid.append(albumi)
        album.append(line[1])
for line in tabel:
    laul = Laul(line[3], line[1], line[0], line[2])
    if line[3] not in l1:
        laulud.append(laul)
        l1.append(line[3])
# mida otsid uuritakse
program = True

# Funktioon, mis  aitab otsida seda mida kasutaja soovib


def otsing1(otsing):
    if otsing == "1":       # Otsing laulja järgi
        print("Keda otsite?")
        artist1 = input()
        for laulja1 in lauljad:
            if artist1 in laulja1.nimi:
                print(laulja1.nimi)
                for a1 in laulja1.albumid:
                    print(a1)

    elif otsing == "2":         # Otsing albumi või aasta järgi
        if otsing == "2":
            print("Mis albumit te otsite?")
            album1 = input()
            for album2 in albumid:
                if album1 in album2.pealkiri:
                    print(album2.pealkiri)
                elif album1 in album2.aasta:
                    print(album2.pealkiri)
    elif otsing == "3":         # Otsing laulu järgi
        if otsing == '3':
            print("Mis laulu te otsite?")
            laul1 = input()
            for laul2 in laulud:
                if laul1 in laul2.pealkiri:
                    print(laul2.pealkiri)
                    print(laul2.album)
                    print(laul2.laulja)
                    print(laul2.aasta)
    elif otsing == "4":         # Väljastab kõik albumid koos sisuga
        print("Albumid on:")
        for album in albumid:
            album.nlauljaJnimi()
            album.nlaulud()
            print("-----------------------------")
    else:
        print("Valige number 1-4!")


while program:
    print("Mida sa otsida tahad?")
    print("1. Artist")
    print("2. Album või aasta")
    print("3. Laul")
    print("4. Kõik albumid")
    uin = input("--> ")
    otsing1(uin)
