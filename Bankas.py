class Bankas:
    #kuriamas konstruktorius
    def __init__(self):
        #sukuriamas tuscias masyvas. listas, kuriame talpinsime visas bankines saskaitas
        self.saskaitos =[]

        #kuriame metoda "Nauja saskaita"
    def nauja_saskaita(self, vardas, pradinis_balansas, numeris):     #sukursime kazkoki varda, pradini balansa, ir to reikes abiem vienu kartu skritingom reiksmem, todel naudosime tuple
        saskaita ={
            "vardas": vardas,
            "balansas": pradinis_balansas,
            "numeris": numeris
        }
             #pridedame saskaita
        self.saskaitos.append(saskaita)
        print("Nauja saskaita sekmingai sukurta")

        #balanso didinimas

    def balanso_didinimas(self, saskaitos_numeris,suma):
            #iteruosime visas saskaitas ir atrasime musu saskaita, kurioje norime padidinti balansa
        for saskaita in self.saskaitos:
                #jei saskaita rasta, padidinsime jos balnsa
            if saskaita["numeris"] == saskaitos_numeris:
                saskaita["balansas"] += suma
                print ("Balansas sekmingai padidintas")
                break
        else:
            print("Nepavyko rasti saskaitos su nurodytu numeriu")

    def isemimas(self, saskaitos_numeris, suma):
        for saskaita in self.saskaitos:
            # jei saskaita rasta, padidinsime jos balnsa
            if saskaita["numeris"] == saskaitos_numeris:
                if saskaita["balansas"] >= suma:
                    saskaita["balansas"] -= suma
                    print("Pinigai sekmingai isimti")
                else:
                    print("Nepakankamas saskaitos likutis")
                    break
        else:
            print("Nepavyko rasti saskaitos su nurodytu numeriu")
       #tikrinsime saskaitos balansa
    def balansas(self, saskaitos_numeris):
        for saskaita in self.saskaitos:
            if saskaita["numeris"] == saskaitos_numeris:
                print(f"Saskaitos balansas: {saskaita['balansas']} Eur")       #balansas naudojame viengubas kabutes, kadangi jau sakinyje yra naudojamos dvigubos kabutes/
                break
        else:
            print("Nepavyko rasti saskaitos su nurodytu numeriu!")

#sukuriame objekta
sebBankas = Bankas()

#naudojame while cikla ir leidziame klientui pasirinkti norima operacija
while True:
    print("Pasirinkite norima veiksma_> ")
    print("1. Sukurti nauja saskaita")
    print("2. Inesti lesas i saskaita")
    print("3. Isimti lesas is saskaitos")
    print("4. Patikrinti saskaitos balansa")
    print("0. Uzbaigti pasirinkimus")
    pasirinkimas = input("Iveskite pasirinkimo numeri_> ")

    #inicijuojame veiksmus
    if pasirinkimas == "1":
        vardas = input("Iveskite varda_> ")
        numeris = input("Iveskite saskaitos numeri_> ")
        pradinis_balansas = float(input("Iveskite pradini balansa_> "))
        # gauname varda ir pradini balansa
        sebBankas.nauja_saskaita(vardas,pradinis_balansas,numeris)
    elif pasirinkimas == "2":
        numeris = input("Iveskite saskaitos numeri_> ")
        suma = float(input("Iveskite inesama suma_> "))
        sebBankas.balanso_didinimas(numeris, suma)
    elif pasirinkimas == "3":
        numeris = input("Iveskite saskaitos numeri_>" )
        suma = float(input("Iveskite isimama suma_> "))
        sebBankas.isemimas(numeris,suma)
    elif pasirinkimas == "4":
        numeris = input("Iveskite saskaitos numeri_> ")
        sebBankas.balansas(numeris)
    elif pasirinkimas == "0":
        break
    else:
        print("Neteisingas pasirinkimas, bandykite dar karta.")
