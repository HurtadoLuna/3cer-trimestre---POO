#sistemas de notas

# class Estudiantes:

#     def __init__(self, nombre, grado, nota):
#        self.nombre = nombre
#        self.grado = grado
#        self.nota = nota

#     def mostrar_info(self):
#         print(f"hola, {self.nombre} :) ")
#         print(f"Su grado es: {self.grado}")
#         print(f"esta fue su nota: {self.nota}")

#         if self.nota >= 3.0:
#             print("usted ha aprobado")
#         else:
#             print("usted reprobo")

# nombre= input("Ingrese su nombre: ")
# grado= input("Ingrese su grado: ")
# nota= float(input("Ingrese su nota:"))

# info= Estudiantes(nombre, grado, nota)
# info.mostrar_info()

# Sistema de votacion 
class Votacion:
    
    def __init__(self, nombre_completo, edad, nacionalidad):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        print(f"nombre completo: {self.nombre_completo}")
        print(f"edad: {self.edad}")
        print(f"nacionalidad: {self.nacionalidad}")

        if self.edad >= 18 and self.nacionalidad == "colombiano":
            print("usted puede votar")
        else:
            print("usted no puede votar")

nombre_completo= input("ingrese su nombre completo:")
edad= int(input("Ingrese su edad: "))
nacionalidad= input("ingrese su nacionalidad: ")

usu= Votacion (nombre_completo, edad, nacionalidad)
usu.mostrar_info()

# 7.1 ¿que clases identificas en el problema?
#     R// se identifica la clase 'Votacion'                                        
# 
# 7.2 ¿que atributos y metodos tendria la clase?
#    R// Atributos: nombre_completo, edad, nacionalidad
#        Métodos: __init__, mostrar_info
# 
# 7.3 ¿que relaciones existen entre ellas?   
#    R// existe una relacion entre Votacion y usu es un objeto que utiliza los atributos y metodos definidos en Votacion                                  
   


