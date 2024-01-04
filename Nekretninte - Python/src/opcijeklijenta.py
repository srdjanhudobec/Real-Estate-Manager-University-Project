import json
def zakup_nekretnine():
    zakup = {}
    from meni_opcije import korIme
    pronadjena = False
    tipUsluge = "/"
    brojevi = [] #za uslov za izabranu opciju
    from meni_opcije import Ime,Prezime
    with open("data/nekretnine.json","r",encoding="utf8") as fp:
        ucitano = json.load(fp)                                   #ovde na pocetku odmah iscitavamo sve fajlove koji ce nam kasnije biti potrebni u metodi
    with open("data/usluge.json","r",encoding="utf8") as fp:
        ucitaneUsluge = json.load(fp)
    tipPretrage = input("Unesite broj ispred kategorije po kojoj zelite da pretrazite nekretninu:\n1.Spram adrese     2.Spram kategorije\n")
    while tipPretrage.strip() != "1" and tipPretrage.strip() != "2": #strip sluzi da se uklone prazna polja tj. space-ovi, ponavlja se unos dok se ne unese odgovarajuca opcija
        tipPretrage = input("Niste uneli odgovarajucu opciju, unesite broj ispred kategorije po kojoj zelite da pretrazite nekretninu:\n1.Spram adrese     2.Spram kategorije\n")
    if tipPretrage == "1": #pretraga spram adrese
        filter = input("Unesite adresu nekretnine: ").lower()  #koristimo metodu .lower() koja sva slova pretvara u mala, da ne bi imali osetljivost na mala i velika sklova prilikom unosa
        for i in range(len(ucitano)):
            tipUsluge = "/"
            adresa = str(ucitano[i]["adresa"])  #izdvajamo adresu
            #print(adresa)
            if adresa.lower().__contains__(filter): #i ovde korisnimo .lower() metodu i sad baratamo samo sa adresom koja je sva napisana malim slovima
                for j in ucitaneUsluge: #ako adresa sadrzi deo unesenog filtera,ispisujemo te nekretnine
                    if j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "zakup": #ako u uslugama postoji nekretnina sa tom sifrom,na osnovu tipa se bira sta ce se ispisati
                        tipUsluge = "zakupljena"
                    elif j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "prodaja":
                        tipUsluge = "prodata"
                ispis = str(i+1) + " " + ucitano[i]["šifra nekretnine"] + " " + ucitano[i]["kategorija"] + " " + ucitano[i]["adresa"] + " " + Ime + " " + Prezime + " " + tipUsluge
                if tipUsluge == "/": #ako se tipUsluge nije menjao, tj. ne postoji u uslugama,to se dodaje kao moguca opcija koju korisnik moze da izabere u listu
                    brojevi.append(str(i+1))
                print(ispis)
                pronadjena = True
            if tipUsluge == "/":
                if i==len(ucitano) - 1 and pronadjena == True and brojevi.count > 0: #ako je pronasao nekretninu i dosao do kraja 
                    nekretnina = input("Unesite broj ispred nekretnine koju hocete da zakupite: ")
                    while brojevi.__contains__(nekretnina.strip()) == False: #ponavljamo unos dok se ne unese odgovarajuca opcija
                        nekretnina = input("Niste uneli odgovarajucu opciju, unesite broj ispred nekretnine koju hocete da zakupite: ")
                    #kreiranje nekretnine za upis u datoteku usluge.json
                    zakup["šifra nekretnine"] = ucitano[int(nekretnina) -1]["šifra nekretnine"]  #kreiramo zakup koji cemo upisati u usluge
                    zakup["korisničko ime agenta"] = ""
                    zakup["korisničko ime klijenta"] = korIme
                    zakup["tip"] = "zakup"
                    zakup["komentar"] = input("Unesite neki komentar: ")
                    usluge = []

                    for k in range(0,len(ucitaneUsluge)):
                        usluge.append(ucitaneUsluge[k])  #na vec procitane usluge dodajemo nov zakup
                    usluge.append(zakup)

                    print(usluge)

                    with open("data/usluge.json","w",encoding="utf8") as fp:       #izmenjenu listu sa dodatim zakupom upisujemo u fajl usluge.json
                        json.dump(usluge,fp,ensure_ascii=False)
            else:
                if tipUsluge == "zakupljena":
                    print("Ne mozete zakupiti pretrazenu nekretninu jer je zakupljena vec.") #ako je nekretnina zakupljena ispisuje se poruka ispod da ne moze da se zakupi vec zakupljena nekretnina
                elif tipUsluge == "prodata":
                    print("Ne mozete zakupiti pretrazenu nekretninu jer je prodata.") #isto vazi i za prodatu nekretninu,ispisuje se ako je nekretnina prodata
        if pronadjena == False:
            print("Ne postoji nekretnina sa unetom adresom. ") #ako ne postoji ni jedna nekretnina sa unetom adresom ispisujemo poruku
    elif tipPretrage == "2":
        tipNekretnine = input("Unesite po kom tipu nekretnine zelite da pretrazite: (stan, kuca, garaza) ")
        while tipNekretnine != "stan" and tipNekretnine != "kuca" and tipNekretnine != "garaza": #isti postupak kao sa adresom,samo se ovde bira na osnovu tipa nekretnine
            tipNekretnine = input("Niste uneli odgovaraci tip, unesite po kom tipu nekretnine zelite da pretrazite: (stan, kuca, garaza) ")
        for i in range(len(ucitano)):
            tipUsluge = "/"
            if ucitano[i]["kategorija"] == tipNekretnine:
                for j in ucitaneUsluge:
                    if j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "zakup":
                        tipUsluge = "zakupljena"
                    elif j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "prodaja":
                        tipUsluge = "prodata"
                ispis = str(i+1) + " " + ucitano[i]["šifra nekretnine"] + " " + ucitano[i]["kategorija"] + " " + ucitano[i]["adresa"] + " " + Ime + " " + Prezime + " " + tipUsluge
                if tipUsluge == "/":
                    brojevi.append(str(i+1))
                print(ispis)
                pronadjena = True
            if tipUsluge == "/":
                if i == len(ucitano) - 1 and pronadjena == True and brojevi.count > 0:
                    nekretnina = input("Unesite broj ispred nekretnine koju hocete da zakupite: ")
                    while brojevi.__contains__(nekretnina.strip()) == False:
                        nekretnina = input("Niste uneli odgovarajucu opciju, unesite broj ispred nekretnine koju hocete da zakupite: ")
                    #kreiranje nekretnine za upis u datoteku usluge.json
                    zakup["šifra nekretnine"] = ucitano[int(nekretnina) -1]["šifra nekretnine"]
                    zakup["korisničko ime agenta"] = ""
                    zakup["korisničko ime klijenta"] = korIme
                    zakup["tip"] = "zakup"
                    zakup["komentar"] = input("Unesite neki komentar: ")
                    usluge = []

                    for k in range(0,len(ucitaneUsluge)):
                        usluge.append(ucitaneUsluge[k])
                    usluge.append(zakup)

                    print(usluge)

                    with open("data/usluge.json","w",encoding="utf8") as fp:      
                        json.dump(usluge,fp,ensure_ascii=False)
            else:
                    if tipUsluge == "zakupljena":
                        print("Ne mozete zakupiti pretrazenu nekretninu jer je zakupljena vec.")
                    elif tipUsluge == "prodata":
                        print("Ne mozete zakupiti pretrazenu nekretninu jer je prodata.")
        if pronadjena == False:
            print("Ne postoji nekretnina sa unetim tipom. ")

def prodaja_nekretnine():  #identican postupak kao i kod zakupa,samo se ovde umesto tipa zakup upisuje u fajl tip prodaja
    zakup = {}
    pronadjena = False
    from meni_opcije import korIme
    tipUsluge = "/"
    brojevi = [] #za uslov za izabranu opciju
    from meni_opcije import Ime,Prezime
    with open("data/nekretnine.json","r",encoding="utf8") as fp:
        ucitano = json.load(fp)
    with open("data/usluge.json","r",encoding="utf8") as fp:
        ucitaneUsluge = json.load(fp)
    tipPretrage = input("Unesite broj ispred kategorije po kojoj zelite da pretrazite nekretninu:\n1.Spram adrese     2.Spram kategorije\n")
    while tipPretrage.strip() != "1" and tipPretrage.strip() != "2": #strip sluzi da se uklone prazna polja tj. space-ovi
        tipPretrage = input("Niste uneli odgovarajucu opciju, unesite broj ispred kategorije po kojoj zelite da pretrazite nekretninu:\n1.Spram adrese     2.Spram kategorije\n")
    if tipPretrage == "1": #pretraga spram adrese
        filter = input("Unesite adresu nekretnine: ").lower()
        for i in range(len(ucitano)):
            tipUsluge = "/"
            adresa = str(ucitano[i]["adresa"])
            #print(adresa)
            if adresa.lower().__contains__(filter):
                for j in ucitaneUsluge:
                    if j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "zakup":
                        tipUsluge = "zakupljena"
                    elif j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "prodaja":
                        tipUsluge = "prodata"
                ispis = str(i+1) + " " + ucitano[i]["šifra nekretnine"] + " " + ucitano[i]["kategorija"] + " " + ucitano[i]["adresa"] + " " + Ime + " " + Prezime + " " + tipUsluge
                if tipUsluge == "/": #moguca opcija su samo brojevi koji nemaju zakup ni prodaju
                    brojevi.append(str(i+1))
                print(ispis)
                pronadjena = True
            if tipUsluge == "/":
                if i == len(ucitano)-1 and pronadjena == True and brojevi.count > 0:
                    nekretnina = input("Unesite broj ispred nekretnine koju hocete da prodate: ")
                    while brojevi.__contains__(nekretnina.strip()) == False:
                        nekretnina = input("Niste uneli odgovarajucu opciju, unesite broj ispred nekretnine koju hocete da prodate: ")
                    #kreiranje nekretnine za upis u datoteku usluge.json
                    zakup["šifra nekretnine"] = ucitano[int(nekretnina) -1]["šifra nekretnine"]
                    zakup["korisničko ime agenta"] = ""
                    zakup["korisničko ime klijenta"] = korIme
                    zakup["tip"] = "prodaja"
                    zakup["komentar"] = input("Unesite neki komentar: ")
                    usluge = []

                    for k in range(0,len(ucitaneUsluge)):
                        usluge.append(ucitaneUsluge[k])
                    usluge.append(zakup)

                    print(usluge)

                    with open("data/usluge.json","w",encoding="utf8") as fp:      
                        json.dump(usluge,fp,ensure_ascii=False)
            else:
                if tipUsluge == "zakupljena":
                    print("Ne mozete prodati pretrazenu nekretninu jer je zakupljena vec.")
                elif tipUsluge == "prodata":
                    print("Ne mozete prodati pretrazenu nekretninu jer je vec prodata.")
        if pronadjena == False:
            print("Ne postoji nekretnina sa unetom adresom. ")
    elif tipPretrage == "2":
        tipNekretnine = input("Unesite po kom tipu nekretnine zelite da pretrazite: (stan, kuca, garaza) ")
        while tipNekretnine != "stan" and tipNekretnine != "kuca" and tipNekretnine != "garaza":
            tipNekretnine = input("Niste uneli odgovaraci tip, unesite po kom tipu nekretnine zelite da pretrazite: (stan, kuca, garaza) ")
        for i in range(len(ucitano)):
            tipUsluge = "/"
            if ucitano[i]["kategorija"] == tipNekretnine:
                for j in ucitaneUsluge:
                    if j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "zakup":
                        tipUsluge = "zakupljena"
                    elif j["šifra nekretnine"] == ucitano[i]["šifra nekretnine"] and j["tip"] == "prodaja":
                        tipUsluge = "prodata"
                ispis = str(i+1) + " " + ucitano[i]["šifra nekretnine"] + " " + ucitano[i]["kategorija"] + " " + ucitano[i]["adresa"] + " " + Ime + " " + Prezime + " " + tipUsluge
                if tipUsluge == "/":
                    brojevi.append(str(i+1))
                print(ispis)
                pronadjena = True
            if tipUsluge == "/":
                if i == len(ucitano)-1 and pronadjena == True and brojevi.count > 0:
                    nekretnina = input("Unesite broj ispred nekretnine koju hocete da prodate: ")
                    while brojevi.__contains__(nekretnina.strip()) == False:
                        nekretnina = input("Niste uneli odgovarajucu opciju, unesite broj ispred nekretnine koju hocete da prodate: ")
                    #kreiranje nekretnine za upis u datoteku usluge.json
                    zakup["šifra nekretnine"] = ucitano[int(nekretnina) -1]["šifra nekretnine"]
                    zakup["korisničko ime agenta"] = ""
                    zakup["korisničko ime klijenta"] = korIme
                    zakup["tip"] = "prodaja"
                    zakup["komentar"] = input("Unesite neki komentar: ")
                    usluge = []

                    for k in range(0,len(ucitaneUsluge)):
                        usluge.append(ucitaneUsluge[k])
                    usluge.append(zakup)

                    print(usluge)

                    with open("data/usluge.json","w",encoding="utf8") as fp:      
                        json.dump(usluge,fp,ensure_ascii=False)
            else:
                if tipUsluge == "zakupljena":
                    print("Ne mozete prodati pretrazenu nekretninu jer je zakupljena vec.")
                elif tipUsluge == "prodata":
                    print("Ne mozete prodati pretrazenu nekretninu jer je vec prodata.")
        if pronadjena == False:
            print("Ne postoji nekretnina sa unetim tipom. ")