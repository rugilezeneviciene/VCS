#------ OBJEKTINIS PROGRAMAVIMAS ---
#Dazniausiai objektas yra vadinamas init. to konstruktoriaus viduje rasomi parametrai (spalva, greitis). Kad tuos parametrus galetume naudoti, reikia padaryti priskyrima self.spalva


class Automobilis:   # mes nurodeme objekta
    def __init__(self, spalva, greitis):    #konstruktorius __init__ self...savybes
        self.spalva = spalva
        self.greitis = greitis
        self.uzvesta = False


    def uzvedam_automobili(self):
        if not self.uzvesta:
            print("Automobilis uzsivede")
            self.uzvesta = True
        else:
            print("Automobilis jau yra uzvestas")

    def didinam_greiti(self, kiekis):    #apsirasem metoda
        self.greitis += kiekis        #self leidzia apibudinti metodus ir parametsus

    def isjungiam_automobili(self):
        if self.uzvesta:
            print("Automobilis isjungtas")
            self.uzvesta = False     #keiciam statusa
        else:
            print("Automobilis jau yra isjungtas")




automobilis = Automobilis("Juoda", 0)    #cia sukurem objekta
automobilis.uzvedam_automobili()
automobilis.didinam_greiti(10)
print(automobilis.greitis)
automobilis.isjungiam_automobili()

print(automobilis.spalva)

honda = Automobilis("Raudona",120)


honda.didinam_greiti(50)
print("Jusu esamas greitis: ", honda.greitis)