from meni_opcije import registracija_korisnika,prijava_korisnika
def main(): #korisnik unosom broja bira jednu od 3 ponudjene opcije
    opcija = input("Dobrodosli u aplikaciju za nekretnine. Unesite broj ispred opcije koju birate:\n1.Prijava korisnika    2.Registracija korisnika    3.Izlazak iz aplikacije \n")
    while opcija != "1" and opcija != "2" and opcija != "3": #dok se ne unese odgovarajuci broj ispred opcije ponavlja se unos dok se ne unese neka od ponudjenih opcija
        opcija = input("Niste uneli odgovarajucu opciju, unesite broj ispred opcije koju birate:\n1.Prijava korisnika    2.Registracija korisnika    3.Izlazak iz aplikacije \n")
    if opcija == "1":
        prijava_korisnika()     #na osnovu unesenog broja se pokrece metoda za opciju koju je korisnik izabrao
    elif opcija == "2":
        registracija_korisnika()
    elif opcija == "3":
        exit()
main() #pozivamo funkciju

