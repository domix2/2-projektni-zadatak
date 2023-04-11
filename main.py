from datetime import date

korisnici = []
kategorije = []
prodaje = []

broj_korisnika = int(input("Unesite broj korisnika:"))

for i in range(1, broj_korisnika + 1):
    korisnik = {}
    korisnik['Ime'] = input(f"Unesite ime {i}. korisnika:").capitalize()
    korisnik['Prezime'] = input(f"Unesite prezime {i}. korisnika:").capitalize()
    korisnik['Telefon'] = int(input(f"Unesite telefon {i}. korisnika:"))
    korisnik['Email'] = input(f"Unesite email {i}. korisnika:").strip()
    korisnici.append(korisnik)

broj_kategorija = int(input("Unesite broj kategorija:"))

for i in range(1, broj_kategorija+1):
    kategorija = {}
    kategorija['naziv'] = input(f'Unesite naziv {i}. kategorije:')
    kategorija['artikli'] = []
    broj_artikala = int(input(f'Unesite broj artikala za {i}. kategoriju:'))

    for j in range(1,broj_artikala+1):
        artikl = {}
        artikl['naslov'] = input(f'Unesite naslov {j}. artikla:')
        artikl['opis'] = input(f'Unesite opis {j}. artikla:')
        artikl['cijena'] = float(input(f'Unesite cijenu {j}. artikla:'))
        kategorija['artikli'].append(artikl)

    kategorije.append(kategorija)

broj_prodaja = int(input('Unesite broj prodaja:'))
for i in range(1,broj_prodaja+1):
    prodaja = {}
    dan = int(input(f'Unesite dan isteka {i}. prodaje:'))
    mjesec = int(input(f'Unesite mjesec isteka {i}. prodaje:'))
    godina = int(input(f'Unesite godinu isteka {i}. prodaje:'))
    prodaja['datum'] = date(godina, mjesec, dan)
    prodaja['artikli'] = artikl

    print(f'Odaberite korisnika {i}. prodaje')
    for j,korisnik in enumerate(korisnici, start =1):
        print(f"\t{j}.{korisnik['Ime']}{korisnik['Prezime']}")
        odabrani_korisnik = int(input('Odabrani korisnik:'))
        prodaja['korisnik'] = korisnici[odabrani_korisnik-1]
    print(f'Odaberite kategoriju {i}. prodaje')
    for j,kategorija in enumerate(kategorije,start = 1):
        print(f"{j}. {kategorija['naziv']}")
        odabrana_kategorija = int(input('Odabrana kategorija:'))
        print(f'Odaberite artikl {i}.prodaje')
for j,artikl in enumerate(kategorije[odabrana_kategorija-1]['artikli'],start =1):
    print(f"{j}. {kategorije[odabrana_kategorija-1]['artikli'][j-1]['naslov']}")

    odabrani_artikl = int(input('Odabrani artikl:'))
    prodaja['artikl']=kategorije[odabrana_kategorija-1]
    prodaje.append(prodaja)

for i,prodaja in enumerate(prodaje, start = 1):
    print(f" {i}. prodaja ")
    print('Informacije o korisniku:')
    print(f"\tIme: {prodaja['korisnik']['Ime']}")
    print(f"\tPrezime: {prodaja['korisnik']['Prezime']}")
    print(f"\tTelefon: {prodaja['korisnik']['Telefon']}")
    print(f"\tEmail: {prodaja['korisnik']['Email']}")
    print('Informacije o artiklu:')
    print(f"\tNaslov: {prodaja['artikli']['naslov']}")
    print(f"\tOpis: {prodaja['artikli']['opis']}")
    print(f"\tCijena: {prodaja['artikli']['cijena']}")
    print('Datum isteka:')
    print(f"\tDan: {prodaja['datum'].day}")
    print(f"\tMjesec: {prodaja['datum'].month}")
    print(f"\tGodina: {prodaja['datum'].year}")
    print('-'*20)

