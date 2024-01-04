import json
import csv
def potvrda_usluge():
    from meni_opcije import korIme as korImeUl   #uzima korisnicko ime ulogovanog
    with open("data/usluge.json","r",encoding="utf8") as fp: #iscitavamo sve usluge iz fajla usluge.json
        usluge = json.load(fp)
    pronadjeno = False
    brojevi = []
    opcijaPretrage = input("Unesite broj ispred opcije po kojoj zelite da pretrazite uslugu:\n1.Po korisnickom imenu klijenta     2.Po sifri nekretnine\n")
    while opcijaPretrage != "1" and opcijaPretrage != "2": #dok se ne unese odgovarajuca opcija ponavljamo unos
        opcijaPretrage = input("Niste uneli odgovarajucu opciju, unesite broj ispred opcije po kojoj zelite da pretrazite uslugu:\n1.Po korisnickom imenu klijenta     2.Po sifri nekretnine\n")
    if opcijaPretrage == "1":
        korImenaKlijenata = []                                          #ako se bira po korisnickom imenu klijenta,iscitavamo sve korisnike i kupimo korisnicka imena svih klijenata koji postoje
        with open("data/korisnici.csv","r",encoding="utf8") as fp:
            korisnici = fp.readlines()
            for i in korisnici:
                podaci = i.split(",")
                if podaci[5].strip() == "klijent":
                    korImenaKlijenata.append(podaci[0])
        korIme = input("Unesite korisnicko ime klijenta: ")
        while korImenaKlijenata.__contains__(korIme) == False:  #dokle god korisnik ne unese korisnicko ime koje postoji u nasoj listi korisnickih imena klijenata,ponavlja se unos
            korIme = input("Ne postoji klijent sa unetim korisnickim imenom, unesite korisnicko ime klijenta: ")
        zaPotvrdu = "" #opcija koju ce kasnije birati korisnik
        for i in range(len(usluge)):
            if usluge[i]["korisničko ime klijenta"] == korIme and usluge[i]["korisničko ime agenta"] == "": #ako se u uslugama nalazi korisnicko ime koje se poklapa sa unesenim korisnickim imenom i ne postoji agent upisan za tu uslugu ispisujemo ga kao opciju koju korisnik moze da potvrdi
                ispis = str(i+1) + " , " + usluge[i]["šifra nekretnine"] + "," + usluge[i]["korisničko ime agenta"] + " , " + usluge[i]["korisničko ime klijenta"] + " , " + usluge[i]["tip"] + " , " + usluge[i]["komentar"]
                print(ispis)
                brojevi.append(str(i+1))    #ispisujemo sve opcije koje se poklapaju sa ulovom i njihove indekse uvecane za 1 smestamo u listu mogucih opcija koje korisnik moze da izabere
                pronadjeno = True
            if i == len(usluge) - 1 and pronadjeno == True:  #ako je dosao do kraja i ispisao bar 1 opciju
                zaPotvrdu = input("Unesite broj ispred usluge koju zelite da potvrdite: ")
                while brojevi.__contains__(zaPotvrdu) == False: #dokle god korisnik ne unese odgovarajuci broj ispred ispisanih opcija ponavlja se unos
                    zaPotvrdu = input("Niste uneli odgovarajucu opciju, unesite broj ispred usluge koju zelite da potvrdite: ")
        if pronadjeno == False:
            print("Ne postoji usluga koja moze da se potvrdi.")
        noveUsluge = [] #lista sa potvrdjenim agentom
        if zaPotvrdu != "": #ako se birala usluga koja ce da se potvrdi onda menjaj
            for j in range(len(usluge)):
                if j == int(zaPotvrdu) - 1:  #kad se u listi usluga dodje do indeksa u kom treba nesto menjati
                    usluga = {}
                    usluga["šifra nekretnine"] = usluge[j]["šifra nekretnine"]
                    usluga["korisničko ime agenta"] = korImeUl                         #kreiranje nove usluge sa izmenjenim korisnickim imenom agenta
                    usluga["korisničko ime klijenta"] = usluge[j]["korisničko ime klijenta"]
                    usluga["tip"] = usluge[j]["tip"]
                    usluga["komentar"] = usluge[j]["komentar"]
                    noveUsluge.append(usluga)
                else:
                    noveUsluge.append(usluge[j]) 
            with open("data/usluge.json","w",encoding="utf8") as fp:      #novu listu sa izmenjenim podacima o agentu upisi u fajl usluge.json
                json.dump(noveUsluge,fp,ensure_ascii=False)
    elif opcijaPretrage == "2":
        index = 0
        sifreNekretnina = []                #identican postupak kao kod korisnickog imena klijenta samo je uslov drugaciji
        zaPotvrdu = ""
        #izdvajamo sve sifre nekretnina koje postoje u uslugama
        for i in usluge:
            sifreNekretnina.append(i["šifra nekretnine"])
        sifraNekretnine = input("Unesite sifru nekretnine: ")
        while sifreNekretnina.__contains__(sifraNekretnine) == False: #dokle god se ne unese postojeca sifra nekretnine ponavlja se unos
            sifraNekretnine = input("Sifra nekretnine koju ste uneli ne postoji u uslugama, unesite sifru nekretnine: ")
        for i in range(len(usluge)):
            if usluge[i]["šifra nekretnine"] == sifraNekretnine and usluge[i]["korisničko ime agenta"] == "":
                ispis = usluge[i]["šifra nekretnine"] + "," + usluge[i]["korisničko ime agenta"] + " , " + usluge[i]["korisničko ime klijenta"] + " , " + usluge[i]["tip"] + " , " + usluge[i]["komentar"]
                print(ispis)
                index = i
                pronadjeno = True
            if i == len(usluge) - 1 and pronadjeno == True:
                noveUsluge = [] #lista sa potvrdjenim agentom
                for j in range(len(usluge)):
                    if j == index:
                        usluga = {}
                        usluga["šifra nekretnine"] = usluge[j]["šifra nekretnine"]
                        usluga["korisničko ime agenta"] = korImeUl
                        usluga["korisničko ime klijenta"] = usluge[j]["korisničko ime klijenta"]
                        usluga["tip"] = usluge[j]["tip"]
                        usluga["komentar"] = usluge[j]["komentar"]
                        noveUsluge.append(usluga)
                    else:
                        noveUsluge.append(usluge[j])
                with open("data/usluge.json","w",encoding="utf8") as fp:      
                    json.dump(noveUsluge,fp,ensure_ascii=False)
        if pronadjeno == False:
            print("Ne postoji usluga koja moze da se potvrdi.")

def stampanje_usluge():
    from meni_opcije import korIme as korImeUl
    brojevi = [] #ovde se nalaze svi indeksi izmedju kojih agent moze da bira koju uslugu hoce da stampa
    uslugaZaStampu = []
    zaStampu = ""
    pronadjeno = False
    with open("data/usluge.json","r",encoding="utf8") as fp:  #iscitavamo sve usluge
        usluge = json.load(fp)
    for i in range(len(usluge)):
        if usluge[i]["korisničko ime agenta"] == korImeUl:  #ako se korisnicko ime ulogovanog agenta poklapa sa korisnickim imenom agenta u uslugama onda se ispisuje
            ispis = str(i+1) + " , " + usluge[i]["šifra nekretnine"] + "," + usluge[i]["korisničko ime agenta"] + " , " + usluge[i]["korisničko ime klijenta"] + " , " + usluge[i]["tip"] + " , " + usluge[i]["komentar"]
            print(ispis)
            brojevi.append(str(i+1)) #ispisuju se usluge koje agent moze da stampa i dodaju se u listu opcija koje korisnik moze da izabere
            pronadjeno = True
        if i == len(usluge) - 1 and pronadjeno == True:
            zaStampu = input("Unesite broj ispred usluge koju zelite da potvrdite: ")
            while brojevi.__contains__(zaStampu) == False:    #dokle god korisnik ne unese odgovarajucu opciju iz liste,ponavlja se unos
                zaStampu = input("Niste uneli odgovarajucu opciju, unesite broj ispred usluge koju zelite da potvrdite: ")
    if pronadjeno == False:  #ako nije nasao ni jednu uslugu koja se poklapa sa uslovom,ispisuje se poruka
        print("Ne postoji usluga koja moze da se stampa.")
    if zaStampu != "": #ako je korisnik imao izbora onda se izabrana usluga kreira
        sifraNekretnine = usluge[int(zaStampu) - 1]["šifra nekretnine"]
        uslugaZaStampu.append(sifraNekretnine)
        uslugaZaStampu.append(usluge[int(zaStampu) - 1]["korisničko ime agenta"])  #kreiramo uslugu i dodajemo je u listu koju cemo upisati u fajl za stampu
        uslugaZaStampu.append(usluge[int(zaStampu) - 1]["korisničko ime klijenta"])
        uslugaZaStampu.append(usluge[int(zaStampu) - 1]["tip"])
        uslugaZaStampu.append(usluge[int(zaStampu) - 1]["komentar"])
        korImeVl = ""
        imeVl = ""
        prezimeVl = ""
        with open("data/nekretnine.json","r",encoding="utf8") as fp: 
            nekretnine = json.load(fp)                           #prvo iz nekretnina vadimo korisnicko ime vlasnika te nekretnine
            for i in nekretnine:
                if i["šifra nekretnine"] == sifraNekretnine:
                    korImeVl = i["korisničko ime vlasnika"]
        with open("data/korisnici.csv","r",encoding="utf8") as fp:
            korisnici = fp.readlines()
            for i in korisnici:
                podaci = i.split(",")
                if podaci[0] == korImeVl:
                    imeVl = podaci[2]                            #onda preko korisnickog imena nalazimo iz fajla korisnici.csv njegovo ime i -prezime
                    prezimeVl = podaci[3]
        if korImeUl != "" and imeVl != "" and prezimeVl != "":  #ako smo uspeli naci vlasnika nekretnine
            with open("data/"+ sifraNekretnine + " - " + imeVl + " " + prezimeVl + ".csv","w",encoding="utf8") as fp:     #upisuje se u fajl pod zahtevanim imenom krajnjalista
                writer = csv.writer(fp)
                writer.writerow(uslugaZaStampu)           #koristi se metoda writerow,koja upisuje podatke iz liste u csv fajl odvojene zarezom
        else:
            print("Nekretnina nema vlasnika.") #ako nismo uspeli naci vlasnika ispisuje se poruka