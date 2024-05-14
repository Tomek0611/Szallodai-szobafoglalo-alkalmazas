from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.foglalasok = []

    def foglalas(self, datum):
        self.foglalasok.append(datum)
        print(f"{self.szobaszam} szoba foglalva {datum} dátumra.")

    def lemondas(self, datum):
        if datum in self.foglalasok:
            self.foglalasok.remove(datum)
            print(f"{self.szobaszam} szoba foglalása törölve {datum} dátumról.")
        else:
            print(f"Nincs foglalás ezen a dátumon a(z) {self.szobaszam} szobára.")

    def ellenorzes(self, datum):
        return datum not in self.foglalasok

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = {}

    def szoba_hozzaadasa(self, szobaszam, ar):
        self.szobak[szobaszam] = Szoba(szobaszam, ar)

    def foglalas(self, szobaszam, datum):
        if szobaszam in self.szobak:
            szoba = self.szobak[szobaszam]
            if szoba.ellenorzes(datum):
                szoba.foglalas(datum)
            else:
                print("Ez a szoba már foglalt ekkorra.")
        else:
            print("Nincs ilyen szoba a szállodában.")

    def lemondas(self, szobaszam, datum):
        if szobaszam in self.szobak:
            self.szobak[szobaszam].lemondas(datum)
        else:
            print("Nincs ilyen szoba a szállodában.")

    def foglalasok_listazasa(self):
        print("Foglalt szobák:")
        for szobaszam, szoba in self.szobak.items():
            if szoba.foglalasok:
                print(f"{szobaszam}: {', '.join(map(str, szoba.foglalasok))}")
            else:
                print(f"{szobaszam}: Nincs foglalás.")

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda

    def foglalas(self, szobaszam, datum):
        self.szalloda.foglalas(szobaszam, datum)

    def lemondas(self, szobaszam, datum):
        self.szalloda.lemondas(szobaszam, datum)

    def foglalasok_listazasa(self):
        self.szalloda.foglalasok_listazasa()

def main():
    szalloda = Szalloda("Példa Szálloda")
    szalloda.szoba_hozzaadasa("101", 100)
    szalloda.szoba_hozzaadasa("201", 150)
    szalloda.szoba_hozzaadasa("202", 150)

    foglalaskezelo = FoglalasKezelo(szalloda)

    foglalaskezelo.foglalas("101", datetime(2024, 5, 1))
    foglalaskezelo.foglalas("201", datetime(2024, 5, 2))
    foglalaskezelo.foglalas("201", datetime(2024, 5, 3))
    foglalaskezelo.foglalas("202", datetime(2024, 5, 2))
    foglalaskezelo.foglalas("202", datetime(2024, 5, 3))

    while True:
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Művelet kiválasztása: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a foglalandó szoba számát: ")
            datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            foglalaskezelo.foglalas(szobaszam, datum)

        elif valasztas == "2":
            szobaszam = input("Adja meg a lemondandó foglalás szoba számát: ")
            datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            foglalaskezelo.lemondas(szobaszam, datum)

        elif valasztas == "3":
            foglalaskezelo.foglalasok_listazasa()

        elif valasztas == "4":
            break

        else:
            print("Érvénytelen művelet.")

if __name__ == "__main__":
    main()