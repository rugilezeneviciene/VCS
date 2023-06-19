class Mokinys:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pazymiai = []

    def prideti_pazymi(self, pazymys):
        self.pazymiai.append(pazymys)


    def skaiciuoti_vidurki(self):
        if len(self.pazymiai) ==0:
            return 0
        else:
            kiekis = len(self.pazymiai)
            suma = sum(self.pazymiai)
            vidurkis = suma/kiekis
            return vidurkis


mokinys1 = Mokinys("Jonas","Jonaitis")
mokinys2 = Mokinys("Petras", "Petraitis")

mokinys1.prideti_pazymi(10)
mokinys1.prideti_pazymi(8)
mokinys1.prideti_pazymi(9)
mokinys1.skaiciuoti_vidurki()
print(f"Mokinio {mokinys1.vardas} pazymiu vidurkis yra {mokinys1.skaiciuoti_vidurki()}")


mokinys2.prideti_pazymi(8)
mokinys2.prideti_pazymi(10)
mokinys2.prideti_pazymi(10)
mokinys2.prideti_pazymi(10)

print(f"Mokinio {mokinys2.vardas} pazymiu vidurkis yra {mokinys2.skaiciuoti_vidurki()}")