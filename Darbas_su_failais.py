# file = open("tekstas.txt", "w")              #"r" - skaito faila, "w" - write, bando irasyti tam tikras reiksmes ]
# content = file.write("Tekstas naujame faile")    #
# print(content)
#
# file = open("tekstas.txt", "r")              #"tekstas naujame faile, kuriam isbandome read funkcija
# content = file.read()    #
# print(content)

# file = open("tekstas.txt", "a", encoding="utf8")              #"a - append. jei yra kazkoks tekstas, naudojame a ir tas turinys bus perrasytas
# content = file.write("pasibandau prideti dar")    #
# file.close()

# with open("tekstas1.txt", "w", encoding="utf8") as file:      #with naudojimas darbui su failais, kad uztikrinti, kad butu tinkamai atidaryti ar uzdaryti, net jei yra isimtys.
#   file.write("Tekstas antrajame faile\n")
#   file.write("Antra eilute\n")                                                          #sis sprendimas yra dazniau naudjamas, jam nereikia close

# filename = input("Iveskite failo pavadinima -> ")     # try ir except blokas
#
# try:
#   with open(filename, "r", encoding="utf8") as file:
#     content = file.read()
#     print("File content: ")
#     print(content)
# except FileNotFoundError:
#   print("file not found")
# except:
#   print("Something went wrong")

#uzduotele sukurti nauja faila ir irasyti i ji duomenis

filename = input("Iveskite sukuriamo failo pavadinima -> ")

try:
  with open(filename, "w", encoding="utf8") as file:
    file.write("Pavyzdiniai duomenys: \n")
    file.write("Vardas: Mantas \n")
    file.write("Pavarde: Markus \n")
    print("Duomenys sekmingai irasyti")
except:
  print("Ivyko klaida irasant duomenis i faila")

