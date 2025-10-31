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


# 7.1 ¿que clases identificas en el problema?
#     R// se identifica la clase 'Votacion'                                        
# 
# 7.2 ¿que atributos y metodos tendria la clase?
#    R// Atributos: nombre_completo, edad, nacionalidad
#        Métodos: __init__, mostrar_info
# 
# 7.3 ¿que relaciones existen entre ellas?   
#    R// existe una relacion entre Votacion y usu es un objeto que utiliza los atributos y metodos definidos en Votacion                                  

# 12. IMPLEMENTACION EN PYTHON
# Sistema de votacion 
# class Votacion:
    
#     def __init__(self, nombre_completo, edad, nacionalidad):
#         self.nombre_completo = nombre_completo
#         self.edad = edad
#         self.nacionalidad = nacionalidad

#     def mostrar_info(self):
#         print(f"nombre completo: {self.nombre_completo}")
#         print(f"edad: {self.edad}")
#         print(f"nacionalidad: {self.nacionalidad}")

#         if self.edad >= 18 and self.nacionalidad == "colombiano":
#             print("usted puede votar")
#         else:
#             print("usted no puede votar")

# nombre_completo= input("ingrese su nombre completo:")
# edad= int(input("Ingrese su edad: "))
# nacionalidad= input("ingrese su nacionalidad: ")

# usu= Votacion (nombre_completo, edad, nacionalidad)
# usu.mostrar_info()

#13. AGREGA ATRIBUTOS, METODOS Y UNA RELACION DE HERENCIA 
# candidato1= "Luis"
# candidato2= "Maria"

# class Votacion:
    
#     def __init__(self, nombre_completo, edad, nacionalidad):
#         self.nombre_completo = nombre_completo
#         self.edad = edad
#         self.nacionalidad = nacionalidad

#     def puede_votar(self):
       
#         return self.edad >= 18 and self.nacionalidad.lower() =="colombia"

#     def mostrar_info(self):
#         print(f"nombre completo: {self.nombre_completo}")
#         print(f"edad: {self.edad}")
#         print(f"nacionalidad: {self.nacionalidad}")

# #clase hija (herencia)
# class VotacionCandidato(Votacion):
#     def __init__(self, nombre_completo, edad,nacionalidad, candidato1, candidato2):
#         super().__init__( nombre_completo, edad, nacionalidad)
#         self.candidato1 = candidato1
#         self.candidato2 = candidato2

#     def mostrar_info(self):
#         super().mostrar_info()
#         print(f"Candidato1 ={candidato1} | Candidato2 = {candidato2}")

# ejecucion
# nombre_completo= input("ingrese su nombre completo:")
# edad= int(input("Ingrese su edad: "))
# nacionalidad= input("ingrese su nacionalidad: ")

# voto = VotacionCandidato (nombre_completo, edad, nacionalidad, candidato1, candidato2)
# voto.mostrar_info()

# if  voto.puede_votar():
#     print("Usted no puede votar porque es menor de edad o no es colombiano")
# else:
#     eleccion_candidato=input("Ingrese el candidato por el que quiere votar: ")
    
#     if eleccion_candidato.lower() == "Luis" or "Maria" :
#         print(f"has votado por el candidato {eleccion_candidato}")
#     else:
#         print("candidato no valido")

# 14. MUESTRA UN EJEMPLO DE POLIMORFISNO EN TU CODIGO
class Votacion:
    
     def __init__(self, nombre_completo, edad, nacionalidad):
         self.nombre_completo = nombre_completo
         self.edad = edad
         self.nacionalidad = nacionalidad

     def puede_votar(self):
       
         if self.edad >= 18 and self.nacionalidad.lower() =="colombia":
               print("usted puede votar")
         else:
             print("usted no puede votar")


     def mostrar_info(self):
         print(f"nombre completo: {self.nombre_completo}")
         print(f"edad: {self.edad}")
         print(f"nacionalidad: {self.nacionalidad}")

 #clase hija 1 - polimorfismo
class VotacionRegional (Votacion):
    def puede_votar(self):
        print("Votacion Regional puede para seleccionar alcaldes y gobernadores")

print("\n SISTEMA DE VOTACION")
nombre_completo= input("ingrese su nombre completo:")
edad= int(input("Ingrese su edad: "))
nacionalidad= input("ingrese su nacionalidad: ")

print("Seleccione el tipo de votacion \n 1. Presidencial \n 2. Regional")

opcion= input("opcion: ")

if opcion == "1":
    persona= Votacion(nombre_completo, edad, nacionalidad)
elif opcion == "2":
    persona= VotacionRegional(nombre_completo, edad, nacionalidad)
else: 
    print("opcion no valida")
   

print("\nRESULTADOS")
persona.mostrar_info()
persona.puede_votar()

    

