# 1 #bandysime atrinkti skaiciusi atrinkti, kurie yra daugiau nei 25.
# skaiciai = [10,20,30,40,50,23]
# atrinkti = []
#
# for skaicius in skaiciai:
#     if skaicius > 25:
#         atrinkti.append(skaicius)
# print("Atrinkti skaiciai: ",atrinkti)

#2# duotu unikalias reiksmes
# skaiciai = [10,10,20,44,50,50,23,23,2,45,44,11,21]
# unikalios_reiksmes = []
#
# for skaicius in skaiciai:
#     if skaicius not in unikalios_reiksmes:
#         unikalios_reiksmes.append(skaicius)
# print(unikalios_reiksmes)

#3# pasisveikinimo funkcija
# def pasisveikinimas(vardas = "sugalvojimas"):
#     print("Labas, ", vardas)
#
# pasisveikinimas("Rugile")

#4# sujungti sarasus

# def sujungti_sarasus(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return(sujungtas_sarasas)
#
# sarasas1 = [1,2,3]
# sarasas2 = [4,5,6]
#
# rezultatas = sujungti_sarasus(sarasas1,sarasas2)
# print(rezultatas)
#5 Parašykite funkciją ar_lyginis, kuri priima vieną skaičių kaip argumentą ir patikrina, ar skaičius yra lyginis.
# Jei skaičius yra lyginis, tada funkcija turi grąžinti True, o jei nelyginis - False.
# def ar_lyginis(skaicius):
#     if skaicius % 2 ==0:
#         return True
#     else:
#         return False
# print(ar_lyginis(7))

#6----Parašykite funkciją didziausias_skaicius, kuri priima sąrašą skaičių ir grąžina didžiausią skaičių iš sąrašo;
# def diddziausias_skaicius(sarasas):
#     didziausias = sarasas [0]
#     for skaicius in sarasas:
#         if skaicius > didziausias:
#             didziausias=skaicius
#     return didziausias
# listas = [1,52,58,95,45,75,105,3,5]
# rezultatas = diddziausias_skaicius(listas)
# print(f"Didziausias skaicius yra {rezultatas}")

#7 --- Parašykite funkciją unikalios_reiksmes, kuri priima sąrašą ir grąžina naują sąrašą,
# kuriame yra tik unikalios reikšmės iš pradinio sąrašo

# def unikalios_reiksmes(sarasas):
#     tuscias_listas = []
#     for reiksme in sarasas:
#         if reiksme not in tuscias_listas:
#            tuscias_listas.append(reiksme)
#
#     return tuscias_listas
# naujas_sar = [5,4,5,4,4,1,1,1,1,25,4,5,8,6,9,7,25]
# rezultatas = unikalios_reiksmes(naujas_sar)
# print(rezultatas)

#8 Apskaičiuokite skaičių sąrašo suma, išskyrus tuos skaičius, kurie yra lyginiai.
# Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina sumą.
# def nelyginiu_suma(sarasas):
#     suma = 0
#     for nelyginis in sarasas:
#         if nelyginis % 2 != 0:
#             suma += nelyginis
#     return suma
#
# listas = [1,1,2,3,4,8,10,12]
# rezultatas = nelyginiu_suma(listas)
# print(rezultatas)
#9.Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis skaičius.

# def ar_pirminis(skaicius):
#     if skaicius <2:
#         return False
#     for daliklis in range(2, skaicius):
#         if skaicius % daliklis == 0:
#             return False
#     else:
#         return True
#
# ivedam = int(input("Iveskite skaiciu, patikrinsime: "))
# if ar_pirminis(ivedam):
#     print(f"Skaicius {ivedam} yra pirminis skaicius")
# else:
#     print (f"Skaicius {ivedam} nera pirminis skaicius")

#10 Uzduotele Reikia paprasyti vartotojo ivesti inputa (int) skaiciu ir atspausdinti visus lyginius skaicius nuo ivesto skaiciaus iki 0
# skaicius = int(input("Iveskite skaiciu: "))
# while skaicius >=0:
#     if skaicius % 2 ==0:
#         print(skaicius)
#     skaicius -=1

#11 Parasyti, ar knyga turi daugiau nei 300 psl.

# class Knyga:
#
#     def __init__ (self, pavadinimas, autorius, puslapiai):
#         self.pavadinimas = pavadinimas,
#         self.autorius = autorius,
#         self.puslapiai = puslapiai
#
#     def tikrinti_puslapius(self):
#         if self.puslapiai > 300:
#             return True
#         else:
#             return False
#
# knyga1 = Knyga("Vakaro knyga", "Rasytoja", 250)
# knyga2 =Knyga("Ryto knyga", "autorius", 450)
#
# print(knyga2.tikrinti_puslapius())

#12 ---Uzduotis padaryti darbutoju sarasa, ir jam padidinti alga tam tikru procentu, pakeisti pavarde ir pan.
# class Darbuotojai:
#     def __init__(self, vardas, pavarde, alga):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.alga = alga
#
#     def didinti_alga(self, procentas):
#         padidinimas = self.alga * procentas / 100
#         self.alga += padidinimas
#
#     def pakeisti_pavarde(self, nauja_pavarde):
#         self.pavarde = nauja_pavarde
#         print("Pavarde pakeista sekmingai")
#
#     def darbuotojo_informacija(self):
#         print("info apie darbuotoja: ")
#         print(f"Vardas: {self.vardas}")
#         print(f"Pavarde: {self.pavarde}")
#         print(f"Alga: {self.alga}")
# darb1 = Darbuotojai ("Jonas", "Jonaitis", 1000)
# darb2 = Darbuotojai ("Petras", "Petraitis", 1500)
#
# darb1.pakeisti_pavarde("Jonaitelis")
# print(f"Darbuotojo nauja pavarde yra {darb1.pavarde}")
# darb1.didinti_alga(75)
# print(f"Datbuotojo {darb1.vardas}  {darb1.pavarde}   atlyginimas yra {darb1.alga}")
#
# print(darb2.darbuotojo_informacija())

#13 uzduotis sukurti klase preke su pavadinimu, kiekiu ir kainu. Reikes pranesti vartotojui
# kad sandelyje nera tokio kiekio prekiu

# class Preke:
#     def __init__(self, pavadinimas, kaina, kiekis):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.kiekis = kiekis
#
#     def ar_pakankamas_kiekis(self, pardavimo_kiekis):
#         if pardavimo_kiekis > self.kiekis:
#             print("Prekiu likutis nepakankamas")
#         else:
#             self.kiekis -= pardavimo_kiekis
#             print(f"Parduota {self.pavadinimas}, {pardavimo_kiekis} vnt")
#
#     def padidinti_likuti(self, padidinimo_kiekis):
#         self.kiekis += padidinimo_kiekis
#         print(f"Padidinta {self.pavadinimas} {padidinimo_kiekis} vnt")
#
# preke1 = Preke("Pienas", 1.2, 8)
# preke2 = Preke("Sviestas", 1.5, 14)
#
# preke1.ar_pakankamas_kiekis(4)
# preke1.padidinti_likuti(80)

#14 uzduotis Kuriame bloga
class Blog:
    def __init__(self):
        self.posts = []

    def create_post(self, title, description):
        post ={
            "title": title,
            "description": description
        }
        self.posts.append(post)
        print ("Blog post succesfully created")

    def display_all_posts(self):
        if not self.posts:
            print("No blog posts founded")
        else:
            for post in self.posts:
                print(f"Title: {post['title']}")
                print(f"Description {post['description']}")
                print("---")

    def update_post(self, title, new_description):
        for post in self.posts:
            if post["title"] == title:
                post["description"] = new_description
                print("Post updated")
                break
        else:
            print("Post was not found")

    def delete_post(self, title):
        for post in self.posts:
            if post["title"] == title:
                self.posts.remove(post)
                print("Post was removed")
        else:
            print("Post was not found")

post1 = Blog()
post1.create_post("Data analysis students run the world", "Once upon a time, several young people decided to spend their summer evenings to become data analysts")
post1.create_post("Data analysis is on TOP", "During last several years demand of data analytics courses inceased significantly")
post1.create_post("Summer goes on", "Despite students occupancy, they decided to enjoy the summer as much as they can")


post1.update_post("Data analysis is on TOP", "During last several years demand of data analytics courses inceased dramatically")
post1.display_all_posts()










