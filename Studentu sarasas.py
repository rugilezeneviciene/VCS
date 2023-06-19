#----KURIAME ZODYNA -- DICTIONARY#
studentu_sarasas = []
while True:
    vardas = input("Irasykite studento varda: ")
    pavarde = input("Irasykite studento pavarde: ")
    amzius = int(input("Irasykite amziu: "))

    studentas = {
        "vardas": vardas,
        "pavarde": pavarde,
        "amzius": amzius
    }
    studentu_sarasas.append(studentas)
    print("Studentas pridetas sekmingai")

    kas_toliau = input("Ar norite prideti dar viena studenta? (taip/ne) ")
    if kas_toliau.lower() != "taip":
        break


print("Prideti studentai: ")
for studentas in studentu_sarasas:
    print(f"Studento vardas yra {studentas['vardas']}")
    print(f"Studento pavarde yra {studentas['pavarde']}")
    print(f"Studento amzius yra {studentas['amzius']}")
    print("---")



# for key, value in zmogus.items():
#     print(key, ":", value)





#
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
