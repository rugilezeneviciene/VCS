class Studentu_vs:
    def __init__(self):
        self.studentai=[]

    #kuriame metoda naujas studentas
    def naujas_studentas(self, studento_id, vardas,pavarde,mokymosi_programa):
        studentas={
            "studento_numeris": studento_id,
            "vardas": vardas,
            "pavarde": pavarde,
            "studijos": mokymosi_programa
        }
            #pridedame studenta
        self.studentai.append(studentas)
        print("Studentas sekmingai uzregistruotas")

            #studentas keicia mokymosi programa
    def programos_keitimas(self,studento_id,naujos_studijos):
        for studentas in self.studentai:
            if studentas["studento_numeris"] == studento_id:
                studentas["studijos"] = naujos_studijos      #kaip darome update
                print("Studento studijos sekmingai pakeistos")
                break
        else:
            print("Nepavyko rasti tokio studento")

    def studento_istrynimas(self, studento_id):
        for studentas in self.studentai:
            if studentas["studento_numeris"] == studento_id:
                self.studentai.remove(studentas)
                print("Studentas pasalintas")
            else:
                print("Nepavyko rsati tokio studento")

    def studento_statusas(self, studento_id):
        for studentas in self.studentai:
            if studentas["studento_numeris"] == studento_id:
                print(f"Studentas {studentas['vardas']} {studentas['pavarde']}, mokymosi programa: {studentas['studijos']}")
            else:
                print("Nepavyko rasti tokio studento")

    def rodyti_visus_studentus(self):
        if not self.studentai:
            print("Studentu nera")
        else:
            print("Studentu sarasas:  ")
            for studentas in self.studentai:
                print(f"Vardas: {studentas['vardas']}")
                print(f"Pavarde {studentas['pavarde']}")
                print(f"Studiju programa: {studentas['mokymosi_programa']}")


manoUniversitetas = Studentu_vs()

while True:
    print("Pasirinkite norima veiksma_> ")
    print("1. Sukurti nauja studenta")
    print("2. Pakeisti studento studiju programa")
    print("3. Istrinti is sarasu studenta")
    print("4. Studento statuso patikrinimas")
    print("5. Parodyti visus studentus")
    print("0 Uzbaigti pasirinkimus")
    pasirinkimas = input("Iveskite veiksmo numeri_> ")

    if pasirinkimas == "1":
        studento_id = int(input("Iveskite studento id_> "))
        vardas = input("Studento vardas_> ")
        pavarde = input("Studento pavarde_> ")
        mokymosi_programa = input("Studento mokymosi programa_> ")

        manoUniversitetas.naujas_studentas(studento_id,vardas,pavarde,mokymosi_programa)

    elif pasirinkimas == "2":
        studento_id = int(input("Iveskite studento ID_> "))
        mokymosi_programa = input("Iveskite nauja studiju programos pavadinima_> ")
        manoUniversitetas.programos_keitimas(studento_id, mokymosi_programa)

    elif pasirinkimas == "3":
        studento_id = int(input("Iveskite studento ID_> "))
        manoUniversitetas.studento_istrynimas(studento_id)

    elif pasirinkimas == "4":
        studento_id = int(input("Iveskite studento ID_>  "))
        manoUniversitetas.studento_statusas(studento_id)

    elif pasirinkimas == "5":
        manoUniversitetas.rodyti_visus_studentus()

    elif pasirinkimas == "0":
        break







