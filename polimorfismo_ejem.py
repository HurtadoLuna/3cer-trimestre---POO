#clase base
class Animal:
    def hablar (self):
        print("los animales hacen un ruido")

#clase hija 1
class Perro (Animal):
    def hablar(self):
        print("el perro dice; Guuuaa guuuaa")

#clase hija 2
class Gato (Animal):
    def hablar(self):
        print("El gato dice; miau miau")

#funcion que muestra el polimorfismo
def hacer_hablar(animal):
    animal.hablar()   
#crear el objeto
perro = Perro()
gato = Gato()

