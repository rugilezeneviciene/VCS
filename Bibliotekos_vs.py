#1Sukurkite klasę "Knyga" su atributais "pavadinimas", "autorius" ir "isduota". Aprašykite konstruktorių,
# kuris inicializuoja šiuos atributus, priskirdamas jiems reikšmes pagal paduotus parametrus.
class Knyga:
    def __init__(self, pavadinimas, autorius, isduota):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.isduota = True

    # 2 Sukurkite metodus "isduoti" ir "grąžinti" klasei "Knyga". Metodas "isduoti" turėtų patikrinti,
    # ar knyga jau yra išduota. Jei taip, išvesti pranešimą "Knyga jau išduota!".
    # Jei ne, pažymėti knygą kaip išduotą ir išvesti pranešimą "Knyga sėkmingai išduota."
    # Metodas "grąžinimas" turėtų patikrinti, ar knyga buvo grąžinta.
    # Jei taip, pažymėti knygą kaip grąžintą ir išvesti pranešimą "Knyga sėkmingai grąžinta."
    # Jei knyga jau yra grąžinta arba niekada nebuvo išduota, išvesti atitinkamą pranešimą.
    def isduoti(self):
        if self.isduota:
            print("Knyga jau isduota!")
        else:
            self.isduota = True
            print("Knyga sekmingai isduota")

    def grazinti(self):
        if not self.isduota:
            print("Knyga sekmingai grazinta")
        else:
            print("Knyga bibliotekoje")

#3 Sukurkite klasę "Biblioteka" su savybėmis "pavadinimas" ir "knygos".
# Aprašykite konstruktorių, kuris inicializuoja šiuos atributus, priskirdamas jiems reikšmes pagal paduotus parametrus.

class Biblioteka():
    def __init__(self,pavadinimas, knygos):
        super().__init__(pavadinimas)
        self.knygos = knygos
        self.knygu_sarasas =[]

    def prideti_knyga(self, knygos):
        self.knygu_sarasas.append(knygos)
        print("Knyga prideta sekmingai")
    def isduoti_knyga(self, pavadinimas):
        if pavadinimas not in self.knygu_sarasas:
            print("Tokios knygos bibliotekoje nera")
        else:
            pavadinimas.isduoti()

    def grazinti_knyga(self, pavadinimas):
        if pavadinimas in self.knygu_sarasas:
            pavadinimas.grazinti()
            print("Dekojame, knyga grazinta")

#4Sukurkite metodus "pridėti_knygą", "išduoti_knygą" ir "grąžinti_knygą" klasei "Biblioteka".
# Metodas "pridėti_knygą" turėtų priimti knygos objektą kaip parametrą ir pridėti jį į bibliotekos knygų sąrašą.
# Metodas "išduoti_knygą" turėtų priimti knygos pavadinimą kaip parametrą, rasti atitinkamą knygą bibliotekos
# knygų sąraše ir iškviesti knygos "isduoti" metodą.
# Metodas "grąžinti_knygą" turėtų priimti
# knygos pavadinimą kaip parametrą, rasti atitinkamą knygą bibliotekos knygų sąraše ir i
# škviesti knygos "grąžinti" metodą.

bibliotekos_objektas = Biblioteka()
bibliotekos_objektas.prideti_knyga("Ryto knyga")


#5 Sukurkite Bibliotekos objektą su pasirinktu pavadinimu.

#6Sukurkite keletą "Knyga" objektų su skirtingais pavadinimais ir autoriais.

#7Panaudokite Bibliotekos metodus, kad pridėtumėte sukurtas knygas į biblioteką, išduotumėte ir grąžintumėte knygas iš bibliotekos.