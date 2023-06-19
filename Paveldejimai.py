# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print("The animal makes a sound")
#
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)        #jis pasiima name is tevines klases, gaunasi kaip rysys
#         self.age = age
#     def make_sound(self):     #metodo perrasymas
#         print("The dog barks")
#
#
# dog=Dog("Bob", 5)
# dog.make_sound()
# print(f"My dog name is {dog.name} " + "and age is " + str(dog.age))

#
# class Vehicle:                               #susikurem transporta su viena savybe BRAN  TEVINE KLAS
#
#     def __init__(self, brand):
#         self.brand = brand
#
#     def start_engine(self):
#         print("Engine started")
#
#     def stop_engine(self):
#         print("Engine stopped")
#
# class Car(Vehicle): #Sukurem dar viena vaika, kuris paveldejo Vehicle savybes
#
#     def drive(self):
#         print("Car is driving")
#
# car = Car("Toyota")
#
# car.start_engine()
# car.drive()
# car.stop_engine()

# #Sukurti zmogu, klase
#
# class Zmogus:                      #sukuriame tevine klase
#     def __init__(self, name, age):   #isvardiname savybes
#         self.name = name               #aprasome savybes
#         self.age = age
#
#     def display_info(self):        #METODAS rodyti informacija apie zmogu
#         print(f"Zmogaus vardas yra {self.name}")
#         print(f"Zmogaus amzius yra {self.age}")
#
# class Darbuotojas(Zmogus):            #Sukuriame vaikine klase (INHERITANCE)
#     def __init__(self, name, age, salary):   #Isvardiname kokias savybes tures darbuotojas
#         super().__init__(name, age)          #nurodome, kurias savybes tures is Zmogus klases
#         self.salary = salary                   #aprasome papildoma darbuotjo savybe
#
#     def display_info(self):
#         super().display_info()      #panaudosiu tevines klases metoda. print vardas, amziu
#         print(f"Darbuotojo atlyginimas yra {self.salary}")
#
# zmogus = Zmogus("Antanukas", 12)         #sukuriame tevines klases objekta
# darbuotojas = Darbuotojas("Jonukas", 25, 2000)    #sukuriame vaikines klases objekta
#
# zmogus.display_info()
# print()
# darbuotojas.display_info()

#Sukurti pirkiniu krepselio funkcionaluma, turime produkta ir krepseli.
#
# class Product:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#
#     def display_info(self):
#         print(f"Produkto pavadinimas yra {self.title} ")
#         print(f"Produkto kaina yra {self.price} Eur ")
#
# class DiscountedProduct(Product):
#     def __init__(self, title, price, discount_percentage):
#         super().__init__(title, price)
#         self.discount_percentage = discount_percentage
#
#     def calculate_discounted_price(self):
#         discount_amount = self.price * (self.discount_percentage / 100)
#         discounted_price = self.price - discount_amount
#         return discounted_price
#
#     def display_info(self):
#         super().display_info()
#         print(f"Nuolaida {self.discount_percentage} % ")
#         print(f"Galutine kaina yra {self.calculate_discounted_price()} Eur")
#
#
# class ShoppingCart(Product):
#     def __init__(self):
#         super().__init__(title=None, price=None) #nedaryti tarpu
#         self.products = []       #kad krepselyje gali buti ne vienas produktas, naudojame list
#
#     def add_product(self, product):
#         self.products.append(product)                          #pridet i lista produktus (is metodo)
#         print(f"Produktas {product.title} pridetas i krepseli")
#
#     def remove_product(self, product):      ##pasalinti produkta is krepselio
#         if product in self.products:
#             self.products.remove(product)
#             print(f"Produktas {product.title} pasalintas is krepselio")
#         else:
#             print(f"Produktas {product.title} nerastas krepselyje")
#
#     def calculate_total_price(self):
#         total_price = 0
#         for product in self.products: #kadangi turime daug produktu, naudojame FOR cikla
#             total_price += product.price
#         return total_price  #return turi buti visada tame paciame lygyje kaip FOR
#
# prod = Product("Pienas", 2.99)
# prod1 = DiscountedProduct("Obuolys", 3.99, 15)
# prod2 = Product("Sviestas", 3.99)
#
# cart = ShoppingCart()
#
# cart.add_product(prod)
# cart.add_product(prod1)
# cart.add_product(prod2)
# print()
#
# for product in cart.products:
#     product.display_info()
#     print()
#
# total_price = cart.calculate_total_price()
# print(f"Bendra krepselio kaina yra {total_price} EUR")
# print()
#
# cart.remove_product(prod)
#
# total_price = cart.calculate_total_price()
# print(f"NAUJA Bendra krepselio kaina yra {total_price} EUR")
# print()
#
# import random
# import time
# studentai = ["Rugile", "Egidijus", "Mantas", "Migle", "Ausrine", "SauliusS", "SauliusA","Tomas",
#              "Vaidas","Jurate","Modestas"]
# random_student = random.choice(studentai)     #kuriame kintamaji
# time.sleep(3)
# print("Atisitiktinai pasirinktas studentas: ", random_student)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):   #naudoti get metoda kad gauti varda
        return self.name
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age
    def set_age(self, age):
        if age >= 0:
           self_age = age
        else:
            print("Amzius negali buti neigiamas")

person = Person("Jonas", 15)

print("name", person.get_name())
print("age", person.get_age())

person.set_name("Petras")
person.set_age(25)

print("New name", person.get_name())
print("New age", person.get_age())
