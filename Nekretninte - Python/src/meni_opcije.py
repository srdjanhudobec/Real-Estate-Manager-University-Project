from opcijevlasnika import dodavanje_nekretnine
from zajednickeopcije import pretraga_nekretnine,prikaz_istorije_zakupa
from opcijeklijenta import zakup_nekretnine,prodaja_nekretnine           #importujemo sve metode koje ce nam kasnije biti potrebne u programu
from opcijeagenta import potvrda_usluge,stampanje_usluge
def registracija_korisnika():
    listaKorImena = []
    listaEmaila = []
    listaKorisnika = []
    with open("data/korisnici.csv","r", encoding="utf-8") as fp:  #iscitavamo sve korisnike iz csv fajla
        korisnici = fp.readlines()
        for i in korisnici:
            podaci = i.split(",")#kako prolazimo kroz sve korisnike tako u odgovarajucu listu dodajemo odgovarajuci podatak
            listaKorImena.append(podaci[0]) #u listu korisnickih imena npr. dodajemo korisnicko ime svakog korisnika kojeg procitamo iz fajla
            listaEmaila.append(podaci[4])       
            listaKorisnika.append(i.strip())        
    korIme = input("Unesite korisnicko ime: ") #korisnik unosi korisnicko ime
    while listaKorImena.__contains__(korIme): #ako to ime postoji u listi korisnickih imena koju smo popunili,ponavlja se unos sve dok se ne unese nepostojece korisnicko ime
        korIme = input("Uneli ste vec postojece korisnicko ime, unesite korisnicko ime: ")
    lozinka = input("Unesite lozinku: ")
    ime = input("Unesite ime korisnika: ")
    prezime = input("Unesite prezime korisnika: ")  #unos ostalih vrednosti koje su potrebne za registraciju
    email = input("Unesite email adresu korisnika: ")
    while listaEmaila.__contains__(email):  #isto kao i za korisnicko ime,ponavlja se unos dokle god korisnik ne unese mejl adresu koja nije vec registrovana
        email = input("Uneli ste vec registrovanu email adresu, unesite email adresu korisnika: ")
    tip = input("Unesite tip korisnika: (klijent, agent, vlasnik) ") #korisnik bira tip korisnika,dokle god se unos razlikuje od ponudjenih tipova ponavlja se unos
    while tip != "klijent" and tip != "agent" and tip != "vlasnik":
        tip = input("Niste uneli odgovarajuci tip korisnika, unesite tip korisnika: (klijent, agent, vlasnik) ")
    korisnik = korIme + "," + lozinka + "," + ime + "," + prezime + "," + email + "," + tip #kreiramo string novog korisnika
    listaKorisnika.append(korisnik) #dodajemo tog korisnika na procitane korisnike iz fajla
    print(listaKorisnika)
    with open("data/korisnici.csv","w", encoding="utf-8") as fp: #novu listu sa dodatim korisnikom upisujemo u fajl
        for i in listaKorisnika:
            fp.write(i + "\n")
    print("Uspesno ste kreirali nalog!")
    print("Prijava korisnika: ")
    prijava_korisnika()          #odmah nakon registracije pozivamo prijavu korisnika

def prijava_korisnika():
    listaKorisnika = []
    listaKorImena = []
    ulogovan = False
    global korIme,Ime,Prezime
    with open("data/korisnici.csv","r",encoding="utf-8") as fp:  #iscitavamo sve korisnike
        procitano = fp.readlines()
        for i in procitano:
            listaKorisnika.append(i.strip())
            podaci = i.split(",")                #kupi sva korisnicka imena zbog provere dal je uneto korisnicko ime koje postoji
            listaKorImena.append(podaci[0])
    while ulogovan == False:  #dokle god se korisnik nije ulogovao,tj. uneo tacno korisnicko ime i lozinku ponavljaj unos
        korIme = input("Unesite korisnicko ime: ")
        while listaKorImena.__contains__(korIme) == False: #ponavlja se unos dokle god se ne unese korisnicko ime koje postoji u fajlu korisnici.csv
            korIme = input("Niste uneli postojece korisnicko ime, unesite korisnicko ime: ")
        lozinka = input("Unesite lozinku: ")
        for i in listaKorisnika: #prolazi kroz sve korisnike
            podaci = i.split(",")
            if podaci[0] == korIme and podaci[1] == lozinka: #ako se uneto korisnicko ime i lozinka poklapaju sa korisnickim imenom i lozinkom nekog korisnika u bazi korisnik je uspesno ulogovan
                print("Uspesno ste ulogovani " + podaci [2])
                Ime = podaci[2]
                Prezime = podaci[3]   #vadimo ime i prezime korisnika koje ce nam trebati kasnije
                if podaci[5] == "klijent":  #na osnovu tipa korisnika nudimo mu opcije kojima moze da pristupi
                    opcija  = input("Unesite broj ispred opcije koju birate:\n1.Zakup nekretnine    2.Prodaja nekretnine    3.Pretraga nekretnine    4.Prikaz istorije zakupa\n")
                    while opcija != "1" and opcija != "2" and opcija != "3" and opcija != "4": #ponavljamo unos dok korisnik ne unese odgovarajuci broj ispred opcije koju bira
                        opcija  = input("Niste uneli odgovarajucu opciju, unesite broj ispred opcije koju birate:\n1.Zakup nekretnine    2.Prodaja nekretnine    3.Pretraga nekretnine    4.Prikaz istorije zakupa\n")
                    if opcija == "1":
                        zakup_nekretnine()
                    elif opcija == "2":
                        prodaja_nekretnine()     #na osnovu unesenog broja pozivamo odgovarajucu metodu
                    elif opcija == "3":
                        pretraga_nekretnine()
                    elif opcija == "4":
                        prikaz_istorije_zakupa()
                elif podaci[5] == "agent":  #identicna stvar kao za klijenta,samo ovde korisnik bira opcije koje se nude agentu
                    opcija  = input("Unesite broj ispred opcije koju birate:\n1.Potvrda usluge    2.Stampanje usluge    3.Pretraga nekretnine    4.Prikaz istorije zakupa\n")
                    while opcija != "1" and opcija != "2" and opcija != "3" and opcija != "4":
                        opcija  = input("Niste uneli odgovarajucu opciju, unesite broj ispred opcije koju birate:\n1.Potvrda usluge    2.Stampanje usluge    3.Pretraga nekretnine    4.Prikaz istorije zakupa\n")
                    if opcija == "1":
                        potvrda_usluge()
                    elif opcija == "2":
                        stampanje_usluge()
                    elif opcija == "3":
                        pretraga_nekretnine()
                    elif opcija == "4":
                        prikaz_istorije_zakupa()
                elif podaci[5] == "vlasnik": #identicna stvar kao za klijenta,samo ovde korisnik bira opcije koje se nude vlasniku
                    opcija  = input("Unesite broj ispred opcije koju birate:\n1.Dodavanje nekretnine    2.Pretraga nekretnine    3.Prikaz istorije zakupa\n")
                    while opcija != "1" and opcija != "2" and opcija != "3" and opcija != "4":
                        opcija  = input("Niste uneli odgovarajucu opciju, unesite broj ispred opcije koju birate:\n1.Dodavanje nekretnine    2.Pretraga nekretnine    3.Prikaz istorije zakupa\n")
                    if opcija == "1":
                        dodavanje_nekretnine()
                    elif opcija == "2":
                        pretraga_nekretnine()
                    elif opcija == "3":
                        prikaz_istorije_zakupa()
                ulogovan = True #ako je sve proslo kako treba, korisnik je ulogovan i while petlja se ne ponavlja
        if ulogovan == False:  #ako se korisnik nije uspeo ulogovati,ispisuje se poruka
            print("Uneti su netacni podaci,probajte opet. ")
    