import json
import random
import string   #koristi se za kreiranje random stringa   
def dodavanje_nekretnine():
    nekretnina = {}
    N = 3
    slova = ''.join(random.choices(string.ascii_uppercase, k=N))  #izdvaja 3 random slova
    brojevi = ''.join(random.choices(string.digits, k=N))       #izdvaja 3 random broja
    spojeni = slova+brojevi                                     #spajanje 3 random slova i 3 random broja
    sifraNekretnine = ''.join(random.sample(spojeni, len(spojeni)))     #mesa slova u samom spojenom stringu da ne bi isli prvo brojevi pa slova ili obrnuto
    
    with open("data/nekretnine.json","r",encoding="utf8") as fp:
        ucitano = json.load(fp)  #iscitava sve nekretnine
        for i in ucitano:
            if len(ucitano) > 0:
                while i["šifra nekretnine"] == sifraNekretnine:
                    sifra = ''.join(random.choices(string.ascii_uppercase, k=N))  #izdvaja 3 random slova
                    brojevi = ''.join(random.choices(string.digits, k=N))       #izdvaja 3 random broja
                    spojeni = sifra+brojevi                                     #spajanje 3 random slova i 3 random broja
                    sifraNekretnine = ''.join(random.sample(spojeni, len(spojeni))) 
    from meni_opcije import korIme
    ulica = input("Unesite ulicu: ")
    broj = input("Unesite broj: ")
    while broj.isdigit() == False: #sa metodom isdigit proveravamo da li je uneti string broj
        broj = input("Niste uneli broj, unesite broj: ")
    mesto = input("Unesite mesto: ")
    celaAdresa = ulica + " " + broj + ", " + mesto #nakon unetih podataka o adresi,sve to spajamo u jedan string odgovarajuceg formata
    tip = input("Unesite tip nekretnine: (stan, kuca, garaza) ")
    while tip != "kuca" and tip != "stan" and tip != "garaza": #dok se ne unese odgovarajuci tip ponavlja se unos
        tip = input("Niste uneli odgovarajuci tip nekretnine, unesite tip nekretnine: (stan, kuca, garaza) ")
    povrsina = input("Unesite povrsinu nekretnine: ")
    while povrsina.isdigit() == False:  #opet koristimo metodu isdigit(),dok se ne unese broj ponavljamo unos
        povrsina = input("Niste uneli broj, unesite povrsinu nekretnine: ")
    nekretnina["šifra nekretnine"] = sifraNekretnine
    nekretnina["korisničko ime vlasnika"] = korIme                       #recnik dobija vrednosti koje ce se upisati u fajl
    nekretnina["adresa"] = celaAdresa
    nekretnina["kategorija"] = tip                
    nekretnina["površina"] = povrsina

    print(nekretnina)
    nekretnine = []

    for i in range(0,len(ucitano)):
        nekretnine.append(ucitano[i])   #na procitane nekretnine dodajemo novo kreiranu nekretninu
    nekretnine.append(nekretnina)

    print(nekretnine)

    with open("data/nekretnine.json","w",encoding="utf8") as fp:  #tu novu listu sa dodatom nekretninom upisujemo u fajl   
        json.dump(nekretnine,fp,ensure_ascii=False)              