# 1 Spausdinti lyginius skaicius nuo 1-10
# skaiciai = range(1,10)
# for skaicius in skaiciai:
#     if skaicius %2 ==0:
#         print(skaicius)
#destytojo budas:

# for skaicius in range(2,11,2):
#     print(skaicius)


#2 Sukurkite sąrašą, kuriame yra keletas skaičių. Naudojant for ciklą, apskaičiuokite sąrašo skaičių sumą.
# sarasas = [2,1,5,5,80]
# skaiciu_suma = 0
# for skaicius in sarasas:
#     skaiciu_suma = sum(sarasas)
# print(skaiciu_suma)


#3.Parašykite programą, kuri atspausdina visus skaičius nuo 1 iki 20, tačiau jei skaičius yra dalijamas iš 3,
# atspausdinkite "Fizz",
# jei skaičius yra dalijamas iš 5, atspausdinkite "Buzz";
#
#
# for reiksme in range(1,21):
#     if reiksme % 3 ==0 and reiksme % 5 ==0:
#         print("FizzBuzz")
#     elif reiksme % 3 ==0:
#         print("Fizz")
#     elif reiksme % 5 ==0:
#         print("Buzz")
#     else:
#         print(reiksme)

#

#4.Sukurkite klasę "KnygosBiblioteka", turinčią atributą "knygos" (sąrašą) ir metodus "pridėti_knygą" ir "rodyti_knygas". Pridėkite funkcionalumą, kad galėtumėte pridėti knygas į sąrašą ir atspausdinti visas bibliotekoje esančias knygas.
# class KnygosBiblioteka:
#     def __init__(self):
#         self.knygos = []
#     def prideti_knyga(self, knyga):
#         self.knygos.append(knyga)
#         print("knyga prideta sekmingai")
#
#     def rodyti_knygas(self):
#         if not self.knygos:
#             print("Bibliotekoje knygu nera")
#         else:
#             for knyga in self.knygos:
#                 print(f"Knyga: {knyga}")
#                 print("---")
#
# knyga1 = KnygosBiblioteka()
# knyga1.prideti_knyga("Ryto knyga")
# knyga1.prideti_knyga("Vakaro knyga")
# knyga1.rodyti_knygas()


# #5.Sukurkite žodyną su prekių pavadinimais ir jų kainomis. Parašykite programą, kuri suskaičiuoja ir atspausdina visų prekių kainų sumą

# prekes = {
#     "obuolys": 1.99,
#     "persikas": 3.29,
#     "agurkai":4.50
# }
# suma = 0
# for kaina in prekes.values():
#     suma += kaina
# print(f"Visu prekiu kainu suma: {suma}")
#
#  6.  nupiesti ta snaigiu trikampi

# aukstis = 5
# eilutes = aukstis+1
# for i in range(1, eilutes +1):    #prideda dar viena eilute
#     print(" " * (eilutes - i), end="") #i - yra kintamasis, kuris isreiskia einamaja iteracija (eilutes nr, raktas).
#     print("*" * (2 * i -1))
# print(" "*(eilutes-1), end="") #end reiskiakad bus is naujos eilutes
# print("|")

