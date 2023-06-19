# ______1 Uzduotis
# class Knyga:
#     def __init__(self, pavadinimas, autorius, puslapiai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.puslapiai = puslapiai
#         #parasyti metoda, ar knyga turi >300 psl.
#
#     def virs_300_psl(self):
#         if self.puslapiai > 300:
#             return True
#         else:
#             return False
#
# Knyga1 = Knyga("Haris Poteris", "Deividas", 600)
# Knyga2 = Knyga("Karsonas, kuris gyvena ant stogo", "Rasytoja", 250)
#
# print(Knyga1.virs_300_psl())
# print(Knyga2.virs_300_psl())

#------2 Uzduotis padaryti darbutoju sarasa, ir jam padidinti alga, pakeisti pavarde ir pan.

# class Darbuotojas:
#     def __init__(self, vardas, pavarde, atlyginimas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.atlyginimas = atlyginimas
#         #parasyti metoda, kuris padidins darbuotoju atlyginima tam tikru proce
#     def padidinti_atlyginima(self, procentai):
#         padidinimas = self.atlyginimas * procentai / 100
#         self.atlyginimas += padidinimas
#
#     def pakeisti_pavarde(self, nauja_pavarde):       #argumentas, veiksmas, kuri keiciame. kviesime sita funkcija ir reikes parasyti nauja pavarde
#         self.pavarde = nauja_pavarde       #cia yra priskyrimas, todel reikia naudoti SELF
#         print("Pavarde pakeista sekmingai")
#
#
#     def darbuotojo_informacija(self):
#         print("Informacija apie darbuotoja: ")
#         print(f"Vardas: {self.vardas}")
#         print(f"Pavarde: {self.pavarde}")
#         print(f"Atlyginimas: {self.atlyginimas}")
#
#
# Darbuotojas1 = Darbuotojas("Jonas","Jonaitis", 1000)
# Darbuotojas1.padidinti_atlyginima(50)
# print(f"Naujas atlyginimas: {Darbuotojas1.atlyginimas}")
# Darbuotojas1.pakeisti_pavarde("Kazlauskas")           #
# print(f"{Darbuotojas1.vardas} {Darbuotojas1.pavarde} , pavarde pasikeite!")
# Darbuotojas1.darbuotojo_informacija()
#
# Darbuotojas2 = Darbuotojas("Juozas","Juozaitis", 1200)
# Darbuotojas2.padidinti_atlyginima(40)
# print(f"{Darbuotojas2.vardas} {Darbuotojas2.pavarde} Naujas atlyginimas: {Darbuotojas2.atlyginimas}")

# 3 UZDUOTIS
# class Preke:
#     def __init__(self, pavadinimas, kaina, kiekis):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.kiekis = kiekis
#         #mum reikia atnaujinti kaina ir pasakyt kad jo nauja kaina yra ..
#
#     def atnaujinti_kaina (self, nauja_kaina):
#         self.kaina = nauja_kaina
#         print(f"{self.pavadinimas} nauja kaina yra {nauja_kaina}")
#
#         # 4 UZDUOTIS - Reikia pranesti pirkejui, kad sandelyje nera tokio kiekio prekiu
#     def ar_pakankamas_kiekis (self, pardavimo_kiekis):
#         if pardavimo_kiekis <=self.kiekis:      #reikia patikritnit kiek yra sandelyje, ir kiek klientas nori nupirkti
#             self.kiekis-= pardavimo_kiekis
#             print(f"Parduota {self.pavadinimas}, {pardavimo_kiekis} vnt")
#         else:
#             print(f"Nepakanka prekiu {self.pavadinimas}")
#
#     def papildyti_likuti(self,padidinimo_skaicius):
#         self.kiekis += padidinimo_skaicius
#         print(f"Padidinta {self.pavadinimas} {padidinimo_skaicius} vnt")
#
#
# Preke1 = Preke("Puodelis", 5.25, 14)
# Preke2 = Preke("Lekste", 10, 21)
#
# Preke1.atnaujinti_kaina(6.78)
# Preke1.ar_pakankamas_kiekis(20)
# Preke1.papildyti_likuti(10)
# print(Preke1.kiekis)
#___________5 BLOGO KURIMAS____
# class Blog:
#     def __init__(self):
#         self.posts = []     #reikia pasidaryti Lista, kuriame bus saugomi irasai/postai
#     #reikia naujo metodo kuris kuria postus
#     def create_post(self, title, description):
#         post = {
#             "title": title,
#             "description": description
#         }
#         self.posts.append(post)
#         print("Record succesfully created")
#
#     def display_all_posts(self):
#         if not self.posts:
#             print("No blog posts found")
#         else:
#             print("Blog posts: ")
#             for post in self.posts:
#                 print(f"Title: {post['title']}")
#                 print(f"Description: {post['description']}")
#                 print("--------")
#
#     def update_post(self, title, new_description):
#         for post in self.posts:
#             if post["title"] == title:    #cia yra salyga, todel turi buti tas pats title ==
#                post["description"] = new_description
#                print("Blog post updated")
#                break
#         else:
#             print("Blog post not found")
#
#     def delete_post(self, title):
#         for post in self.posts:
#             if post["title"] == title:
#                 self.posts.remove(post)
#                 print("Post was removed")
#                 break
#         else:
#             print("Post was not found")
#
# post1 = Blog() #naudojame ta pati objeta, nes jis neturi atributu
# post1.create_post("Data analysis students run the world", "Once upon a time, several young people decided to spend their summer evenings to become data analysts")
# post1.create_post("Data analysis is on TOP", "During last several years demand of data analytics courses inceased significantly")
# post1.create_post("Summer goes on", "Despite students occupancy, they decided to enjoy the summer as much as they can")
#
# post1.update_post("Data analysis students run the world", "Once upon a time, several young people decided to spend their summer mornings to become data analysts" )
#
# post1.delete_post("Data analysis students run the world")
# post1.display_all_posts()
# #CRUD create,read, update, delete.

#----KURIAME ZODYNA -- DICTIONARY
# zmogus = {      #kuriame vienam zmogui.
#     "vardas": "Jonas",
#     "amzius": 27,
#     "miestas": "Vilnius"
# }
# print("Mano vardas: ", zmogus['vardas'])
#
# #pridedame papildoma apibudinima
# zmogus["lytis"] = "Vyras"
#
# print("As esu ", zmogus["lytis"])
#
# zmogus["amzius"]=20
# print("Atsiprasau, man yra: ", zmogus["amzius"], "metu")
#
# #triname reiksmes
# del zmogus["miestas"]
# print([zmogus])
#
# #jei reiketu pasivaikscioti po visuos siuos elementus, mums reiketu FOR
# for key, value in zmogus.items():
#     print(key, ":", value)

#_____TUPLE__
koordinates = (10,50)      #indeksai tokie patys kaip list, siuo atveju 10 yra 0 . reiksmius (10, 50keisti negalime). nekintantis, nekeiciamas objektu sarasas. elementu reiksmes nemodifikuojamoss po tuple sukurimo
print(koordinates[1])       #naudojame tuple, norint uztikrinti, kad duomenys nebus pakite.

koordinates1 = (54,42,12)
sujungtos_koordinates = koordinates + koordinates1
print(sujungtos_koordinates)