# vardas = "Rugile"
# amzius = 35
# # print(vardas)
# # print(amzius)
#
# # komentuoja viena eilute
# """
# Multi komentarui, kai nori aprasyti  kelias eilutes
# """
#
# # arVartotojasAktyvus = False
#
# #camel case, pirma raide mazoji, po to rasoma is didziosios)
#
#
# #Kad suzinoti, koks duomenu tipas:
# # print(type(amzius))
# # print(type(arVartotojasAktyvus))
# # #Boolean
# #
# # produktoKaina = 3.99
# # #float - kad turi po kablelio skaiciu
# # print(type(produktoKaina))
# miestai = ["Vilnius", "Kaunas", "Klaipeda", 7, 3.5]
# # # suskaiciuoti kokio ilgio sarasas LEN
# # print(len(miestai))
# # # #list. reiksmiu gali buti daug, jos gali buti ivarios, skaiciai, textines reiksmes
# # print(miestai)
# #
# # #indexavimas listo  ["Vilnius", "Kaunas", "Klaipeda"] , 0 reiksme bus Vilnius, pradedame skaiciuoti nuo 0
# # #jei parasysiu -1, rodys Klaipeda
# # print(miestai[-1])
# #
# # #pakeisti miesta:
# # miestai[1]="Siauliai"
# # print(miestai)
# #ir tuomet jau parodo pasikeitusi miesta
#
# #prideti nauja miesta APPEND
# miestai.append("Panevezys")
# # print(miestai)
#
# miestai.insert(1, "Anyksciai")
# print(miestai)
# miestai.pop()
# #issitrina paskutinis irasas
# del miestai [0]
# print(miestai)
# #concatination
# # miestai= ["Vilniuje", "Kaune", "Klaipedoje"]
# print("Mano vardas " + vardas + " As gyvenu " + miestai[0] + " mano amzius " +str(amzius))
# #zodziu sujungime turime  naudoti tik textines reiksmes, todel amzius buvo pakeista i str.

# IF SALYGOS

# if amzius >=18:
#     print("Pilnametis")
# else:
#     print("Nepilnametis")

#sustoja ties ta salyga, kuria atitinka ELIF
# if amzius == 18:
#     print("Pilnametis")
# elif amzius ==24:
#     print("Dvamketuri")
# elif amzius >= 24:
#     print("Daugiau nei 25")
# else:
#     print("Nepilnametis")

# skaicius = -10
# if skaicius >=0:
#     print("Skaicius yra teigiamas arba nulis")
# else:
#     print("Skaicius yra neigiamas")
# ###nepavyko
# skaiciuSarasas = [1,3,53,123,1245,12312]
#
# if len(skaiciuSarasas) > 0:
#     print("Skaiciu sarasas pilnas")
# else:
#     print("Skaisciu sarasas tuscias")

# pasiziuri ar yra sarase IF ZODIS IN ....
# zodis = "Ignalina"
# miestai2 =["Vilniuje", "Kaunas","Klaipeda"]
#
# if zodis in miestai2:
#     print("Zodis "+ zodis + " egzistuoja sarase")
# else:
#     print("Zodis nerastas")

#vartotojui leidzia ivesti skaiciu reiksme:
# skaicius = int(input("Iveskite skaiciu: "))
#
# if skaicius > 0:
#     print("Skaicius yra teigiamas")
# elif skaicius < 0:
#     print("Skaicius yra neigiamas")
# else:
#     print ("Skaicius yra nulis")
""" 
OPERATORIAI
priskyrimo
= priskiriate reiksmei
+= prideda ir priskiria (pvz kaip isspresit uzduoti, bus pridetas taskas)
-= atima ir priskiria
*=
/=
%= liekana
MATEMATINIAI OPERATORIAI
+
-
*
/
%
** kelimas laipsniu
// sveikoji dalyba dalini sveika is sveiko

PALYGINIMO OPERATORIAI
== lygu
!= nelygu
<,>,>=,<=

LOGINIAI OPERATORIAI
and
or 
not
NARYSTES OPERATORIAI (MEMBERSHIP)
in (priklauso)
not in (nepriklauso)

TAPATUMO IDENTITY OPERATORS
is
is not (galima klausti, ar sitavartotojas prisijunges is authenticated? atsakymas taip arba ne"

"""
# 1 UZDUOTIS: Patikrinkite, ar studentas išlaikė egzaminą.

# pazymiai = 8
# if pazymiai == 10:
#     print("islaike puikiai")
# elif pazymiai >=5:
#     print("islaike")
# else:
#     print("neislaike")
#2 UZDUOTIS: Patikrinkite, ar skaičius yra lyginis;
# skaiciai = 10
# if skaiciai % 2 == 0:    # % 2 skaitoma, kaip liekana, dalinant is dvieju yra nulis
#     print("Lyginis skaicius")
# else:
#     print("Nelyginis")
#jei su input
# skaiciai = int(input("Iveskite skaiciu   "))
# if skaiciai % 2 == 0:    # % 2 skaitoma, kaip liekana, dalinant is dvieju yra nulis
#     print("Lyginis skaicius")
# else:
#     print("Nelyginis")

#3 UZDUOTIS: Patikrinkite, ar sąraše yra bent du skaičiai;
# sarasas = [1,2,3,4,5,6,7,8,9,10,11,12]
# if len(sarasas) >=2:
#     print("Yra")
# else:
#     print("Nera")

#FOR CIKLAS

# for i in range(1,11): #paskutinio skaitmens neima.
#     print(i)
#
# vardai = ["Jonas", "Saulius", "Marius", "Rugile"]
#
# #    key       value
# for vardas in vardai:
#     print(vardas)
#     #rasome cikla, kuris eina per kiekviena elementa ir spausdina. Rado Jona, eina toliau.  vardas yra raktas per kuri pasiekia.Kad veiktu print(vardas), reikia nurodyti FOR.
    #-----------------------------------------
# skaiciai = [10,20,30,40,50,23]
# atrinkti = []
#
# #bandysime atrinkti skaiciusi atrinkti, kurie yra daugiau nei 25.
# for skaicius in skaiciai:
#     if skaicius > 25:
#         atrinkti.append(skaicius)   #musu raktas yra skaicius, jis eina per visa sarasa. Tik raktas gali pasiekti teisingas reiksmes, tam mes ji ir sukuriam.
# print("Atrinkti skaiciai: ", atrinkti)
#----------------------------------------------
# duotu unikalias reiksmes
# skaiciai = [10,10,20,44,50,50,23,23,2,45,44,11,21]
# unikalios_reiksmes = []
#
# for skaicius in skaiciai:
#     if skaicius not in unikalios_reiksmes:     #not in panaikina pasikartojancias reiksmes, eina is kaires i desines.
#         unikalios_reiksmes.append(skaicius)
# print("Unikalios reiksmes: ", unikalios_reiksmes)
#------------------------------------
#Funkcijos leidzia strukturuoti koda.
#apsirasoma zodeliu def, tada suteikiamas vardas, skliaustai, juose argumentai (pvz du skaiciai a,b) ir dvitaskis
#kad funkcija grazintu reiksmes, naudojame RETURN
# 1PAVYZDYS   def suma(a, b):
#     return a+b
# #iseiname, kad def butu viename lygyje su rezultatu ir iskvieciame savo def.
# rezultatas = suma(2,5)
# print("Suma: ", rezultatas)

# 2PAVYZDYS
# def pasisveikinimas(vardas = "Anonimas"):
#     print("Labas, ", vardas)
#
# pasisveikinimas("Modestas")

# 3PAVYZDYS
# def sujungti_sarasus(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas      #jei nebutu return, negautume sujungtu reiksmiu.
#
# rezultatas = sujungti_sarasus([1,2,3],[4,5,6])
# print("Sujungtas sarasas: ", rezultatas)
#
# lokalus kintamasis - tik funkcijoje
# globalus - nesvarbu ar yra fukcijoje, ji galima bus surasti

#4 UZDUOTELE ---------Parašykite funkciją ar_lyginis, kuri priima vieną skaičių kaip argumentą ir patikrina, ar skaičius yra lyginis.
# --------------------Jei skaičius yra lyginis, tada funkcija turi grąžinti True, o jei nelyginis - False.
# def ar_lyginis(skaicius):
#
#     if skaicius % 2 == 0:
#         return True
#     else:
#         return False
# print (ar_lyginis(9))

#5 UZDUOTELE ----Parašykite funkciją didziausias_skaicius, kuri priima sąrašą skaičių ir grąžina didžiausią skaičių iš sąrašo;

# def didziausias_skaicius(sarasas):
#     didziausias = sarasas [0] #indexuojam kad suprastu,kad tikriname nuo pirmo skaiciaus liste.
#     for skaicius in sarasas:                    #turime eiti per sarasa ir ieskoti didziausio skaiciaus
#         if skaicius > didziausias:
#             didziausias = skaicius
#     return didziausias
#
# skaiciai = [1,8,9,2,5,7,14,25,45,28,104,5,7,3]
# rezultatas = didziausias_skaicius(skaiciai)
# print(rezultatas)

# 6 UZDUOTELE --- Parašykite funkciją unikalios_reiksmes, kuri priima sąrašą ir grąžina naują sąrašą,
# kuriame yra tik unikalios reikšmės iš pradinio sąrašo

# def unikalios_reiksmes(sarasas):
#     tuscias_listas = []
#     for reiksme in sarasas:    #imamme savo argumenta
#         if reiksme not in tuscias_listas:     #patikriname ar dar nera
#             tuscias_listas.append(reiksme)
#
#     return tuscias_listas
# naujas_sarasas = [1,2,5,5,8,7,8,9,5,8,2,1,2]
# print(unikalios_reiksmes(naujas_sarasas))


# Namu darbo uzduotis:
# #Apskaičiuokite skaičių sąrašo suma, išskyrus tuos skaičius, kurie yra lyginiai.
# Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina sumą.

# def suma_nelyginiu(sarasas):
#     suma =0
#     for nelyginis_skaicius in sarasas:
#         if nelyginis_skaicius % 2 != 0:
#             suma += nelyginis_skaicius     #   += yra incrementas, vadinasi jis eis per pradini sarasa ir prides po viena.
#     return suma
#
# pradinis_sarasas = [1,5,2,8]
# rezultatas = suma_nelyginiu(pradinis_sarasas)
# print(rezultatas)

# 3.Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis skaičius. 1)pradzioje reikia susikurti funkcija.

# def pirminis_skaicius (skaicius):
#     if skaicius <2:    # 1 nera pirminis
#         return False
#     for daliklis in range (2, skaicius):
#         if skaicius % daliklis == 0:        #daliklis - paimtas is for %
#             return False
#     return True
# skaicius = 101
# if pirminis_skaicius(skaicius):
#     print(f"skaicius {skaicius} yra pirminis skaicius")  # f raidele reiskia formatavimasir leidzia ideti teksta ir kintamaji.
# else:
#     print(f"skaicius {skaicius} yra ne pirminis skaicius")


#--------------WHILE----
skaicius = 1
while skaicius <= 5: #tikrins tol, kol jis bus mazesnis nei 5
        print(skaicius)
        skaicius += 1

# Uzduotele Reikia paprasyti vartotojo ivesti inputa (int) skaiciu ir atspausdinti visus lyginius skaicius nuo ivesto skaiciaus iki 0
# skaicius = int(input("Iveskite skaiciu:   "))
# while skaicius >=0:
#     if skaicius % 2 == 0:
#         print(skaicius)
#     skaicius -= 1       #kad eitu is kito galo, mazina vienetu.

#------ OBJEKTINIS PROGRAMAVIMAS ---
#Dazniausiai objektas yra vadinamas init. to konstruktoriaus viduje rasomi parametrai (spalva, greitis). Kad tuos parametrus galetume naudoti, reikia padaryti priskyrima self.spalva

# class Automobilis:
#     def __init__(self, spalva, greitis):
#         self.spalva = spalva
#         self.greitis = greitis
#
# automobilis = Automobilis("Juoda", 100)
# print(automobilis.spalva)
#

#YRA spec metodas saukti funkcijoms.

# if __name__=='__main__':
#     sujungti_sarasus(sarasas1, sarasas2)