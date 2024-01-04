import json
def pretraga_nekretnine():
    pronadjena = False
    tipUsluge = "/"
    from meni_opcije import Ime,Prezime
    with open("data/nekretnine.json","r",encoding="utf8") as fp:
        ucitano = json.load(fp)                               #iscitavamo sve fajlove koji ce nam kasnije biti potrebni
    with open("data/usluge.json","r",encoding="utf8") as fp:
        ucitaneUsluge = json.load(fp)
    tipPretrage = input("Unesite broj ispred kategorije po kojoj zelite da pretrazite nekretninu:\n1.Spram adrese     2.Spram kategorije\n")
    while tipPretrage.strip() != "1" and tipPretrage.strip() != "2": #strip sluzi da se uklone prazna polja tj. space-ovi
        tipPretrage = input("Niste uneli odgovarajucu opciju, unesite broj ispred kategorije po kojoj zelite da pretrazite nekretninu:\n1.Spram adrese     2.Spram kategorije\n")
    if tipPretrage == "1": #pretraga spram adrese
        filter = input("Unesite adresu nekretnine: ").lower()   #objasnjeno sve detaljno kod opcije zakup nekretnine u opcijama klijenta gde se ova pretraga nadogradila sa zakupom
        for i in range(len(ucitano)):
            adresa = str(ucitano[i]["adresa"])
            #print(adresa)
            if adresa.lower().__contains__(filter):
                for j in ucitaneUsluge:
                    if j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "zakup":
                        tipUsluge = "zakupljena"
                    elif j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "prodaja":
                        tipUsluge = "prodata"
                ispis = str(i+1) + " " + ucitano[i]["šifra nekretnine"] + " " + ucitano[i]["kategorija"] + " " + ucitano[i]["adresa"] + " " + Ime + " " + Prezime + " " + tipUsluge
                print(ispis)
                pronadjena = True
        if pronadjena == False:
            print("Ne postoji nekretnina sa unetom adresom. ")
    elif tipPretrage == "2":
        tipNekretnine = input("Unesite po kom tipu nekretnine zelite da pretrazite: (stan, kuca, garaza) ")
        while tipNekretnine != "stan" and tipNekretnine != "kuca" and tipNekretnine != "garaza":
            tipNekretnine = input("Niste uneli odgovaraci tip, unesite po kom tipu nekretnine zelite da pretrazite: (stan, kuca, garaza) ")
        for i in range(len(ucitano)):
            if ucitano[i]["kategorija"] == tipNekretnine:
                for j in ucitaneUsluge:
                    if j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "zakup":
                        tipUsluge = "zakupljena"
                    elif j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "prodaja":
                        tipUsluge = "prodata"
                ispis = str(i+1) + " " + ucitano[i]["šifra nekretnine"] + " " + ucitano[i]["kategorija"] + " " + ucitano[i]["adresa"] + " " + Ime + " " + Prezime + " " + tipUsluge
                print(ispis)
                pronadjena = True
        if pronadjena == False:
            print("Ne postoji nekretnina sa unetim tipom. ")

def prikaz_istorije_zakupa():    
    with open("data/korisnici.csv","r",encoding="utf8") as fp:
            korisnici = fp.readlines() #vadi sve korisnike iz csv fajla
    opcije = input("Unesite broj ispred opcije po kojoj hocete da pretrazite nekretnine za koje cete prikazati istoriju zakupa:\n1.Spram korisnika     2.Spram nekretnine\n")
    while opcije != "1" and opcije != "2":
        opcije = input("Niste uneli odgovarajucu opciju, unesite broj ispred opcije po kojoj hocete da pretrazite nekretnine za koje cete prikazati istoriju zakupa:\n1.Spram korisnika     2.Spram nekretnine\n")
    if opcije == "1":
        korImenaKlijenata = []
        for i in korisnici: #vadi korisnicka imena iz liste
            podaci = i.split(",")
            if podaci[5].strip() == "klijent":
                korImenaKlijenata.append(podaci[0])
        korImeKl = input("Unesite korisnicko ime klijenta: ")
        while korImenaKlijenata.__contains__(korImeKl) == False: #izdvajamo sva korisnicka imena klijenata iz fajla,dokle god se ne unese postojece korisnicko ime klijenta ponavlja se unos
            korImeKl = input("Ne postoji klijent sa unetim korisnickim imenom, unesite korisnicko ime klijenta: ")
        with open("data/usluge.json","r",encoding="utf8") as fp:
            usluge = json.load(fp)
        for i in range(len(usluge)):
            imeAg = ""
            prezAg = ""
            emailAg = ""
            imeKl = ""
            prezKl = ""
            emailKl = ""
            if usluge[i]["korisničko ime klijenta"] == korImeKl and usluge[i]["tip"] == "zakup": #ako se korisnicko ime klijenta poklapa sa procitanom uslugom u for petlji
                for j in korisnici:
                    podaci = j.split(",")
                    if podaci[0] == usluge[i]["korisničko ime klijenta"]:#vadimo ime prezime i email agenta na osnovu korisnickog imena klijenta iz korisnici.csv fajla  
                        imeKl = podaci[2]
                        prezKl = podaci[3]
                        emailKl = podaci[4]
                    elif podaci[0] == usluge[i]["korisničko ime agenta"]:#isto radimo i za agenta ako postoji
                        imeAg = podaci[2]
                        prezAg = podaci[3]
                        emailAg = podaci[4]
                if usluge[i]["korisničko ime agenta"] == "": #ako je polje za korisnicko ime agenta prazno dodajemo / kao znak da ne postoji
                    usluge[i]["korisničko ime agenta"] = "/"
                ispis = usluge[i]["šifra nekretnine"] + " " + usluge[i]["korisničko ime agenta"] + " " + imeAg + " " + prezAg + " " + emailAg + " " + usluge[i]["korisničko ime klijenta"] + " " + imeKl + " " + prezKl  + " " + emailKl + " " + usluge[i]["tip"] + " " + usluge[i]["komentar"]
                print(ispis) #ispisujemo istoriju zakupa u zadatom formatu
    elif opcije == "2":
        pronadjena = False
        with open("data/nekretnine.json","r",encoding="utf8") as fp:
            ucitano = json.load(fp)
        with open("data/usluge.json","r",encoding="utf8") as fp:   #identicnu stvar radimo kao i malopre,samo ovde koristimo pretragu nekretnine i onda nakon pretrage se ispisuje istorija zakupa
            usluge = json.load(fp)
        tipPretrage = input("Unesite broj ispred kategorije po kojoj zelite da pretrazite nekretninu:\n1.Spram adrese     2.Spram kategorije\n")
        while tipPretrage.strip() != "1" and tipPretrage.strip() != "2": #strip sluzi da se uklone prazna polja tj. space-ovi
            tipPretrage = input("Niste uneli odgovarajucu opciju, unesite broj ispred kategorije po kojoj zelite da pretrazite nekretninu:\n1.Spram adrese     2.Spram kategorije\n")
        if tipPretrage == "1": #pretraga spram adrese
            filter = input("Unesite adresu nekretnine: ").lower()
            for i in range(len(ucitano)):
                imeAg = ""
                prezAg = ""
                emailAg = ""
                imeKl = ""
                prezKl = ""
                emailKl = ""
                adresa = str(ucitano[i]["adresa"])
                #print(adresa)
                if adresa.lower().__contains__(filter):
                    for j in usluge:
                        if j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "zakup":
                            for k in korisnici:
                                podaci = k.split(",")
                                if podaci[0] == j["korisničko ime klijenta"]:
                                    imeKl = podaci[2]
                                    prezKl = podaci[3]
                                    emailKl = podaci[4]
                                elif podaci[0] == j["korisničko ime agenta"]:
                                    imeAg = podaci[2]
                                    prezAg = podaci[3]
                                    emailAg = podaci[4]
                            if j["korisničko ime agenta"] == "":
                                j["korisničko ime agenta"] = "/"
                            ispis = j["šifra nekretnine"] + " " + j["korisničko ime agenta"] + " " + imeAg + " " + prezAg + " " + emailAg + " " + j["korisničko ime klijenta"] + " " + imeKl + " " + prezKl  + " " + emailKl + " " + j["tip"] + " " + j["komentar"]
                            print(ispis)
                            pronadjena = True
            if pronadjena == False:
                print("Ne postoji nekretnina sa unetom adresom. ")
        elif tipPretrage == "2":
            tipNekretnine = input("Unesite po kom tipu nekretnine zelite da pretrazite: (stan, kuca, garaza) ")
            while tipNekretnine != "stan" and tipNekretnine != "kuca" and tipNekretnine != "garaza":
                tipNekretnine = input("Niste uneli odgovaraci tip, unesite po kom tipu nekretnine zelite da pretrazite: (stan, kuca, garaza) ")
            for i in range(len(ucitano)):
                imeAg = ""
                prezAg = ""
                emailAg = ""
                imeKl = ""
                prezKl = ""
                emailKl = ""
                if ucitano[i]["kategorija"] == tipNekretnine:
                    for j in usluge:
                        if j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "zakup":
                            for k in korisnici:
                                podaci = k.split(",")
                                if podaci[0] == j["korisničko ime klijenta"]:
                                    imeKl = podaci[2]
                                    prezKl = podaci[3]
                                    emailKl = podaci[4]
                                elif podaci[0] == j["korisničko ime agenta"]:
                                    imeAg = podaci[2]
                                    prezAg = podaci[3]
                                    emailAg = podaci[4]
                            if j["korisničko ime agenta"] == "":
                                j["korisničko ime agenta"] = "/"
                            ispis = j["šifra nekretnine"] + " " + j["korisničko ime agenta"] + " " + imeAg + " " + prezAg + " " + emailAg + " " + j["korisničko ime klijenta"] + " " + imeKl + " " + prezKl  + " " + emailKl + " " + j["tip"] + " " + j["komentar"]
                            print(ispis)
                            pronadjena = True
            if pronadjena == False:       #ukoliko nekretnina ne postoji,ispisuje se poruka
                print("Ne postoji nekretnina sa unetom adresom. ")