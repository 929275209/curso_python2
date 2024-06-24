#return devuelve valores que podre hacer uso 
#print solo muestra por tyerminal

#crear una funcion que retorne el numero 10 y muestre por pantalla
# por terminal si es par.

# def diez():
#     return 11
# if diez()%2==0:
#     print("el numero es par")
# else:
#     print("el numero es impar")
# #print solo muestra por pantalla


##return - cuando queremos que nuestra funcion o RETORNE
# un tipo de dato a un tipo de dato estructurado

# #crear una funcion que me muestre el producto de dos numeros 
# def producto(a,b):
#     return a*b


# #crear una funcion que me retorne una lista d tres numeros
# # 
#  def lista_numero():
#     return [2,5,6]



# #crear una funcion que por parametro reciba
# #un nombre y retorne un MENSAJE de vienvenida con el nombre
# def mensaje(nombre):
#     print(f"hola, {nombre}, vienvenidos")



#crear una funcion que reciba por parametro una lista de numeros
# y que devuelva el numero menor, mostrar por terminal el valor retornado
# por la funcion.

# lista=[1,5,3,9,56]
# def min(1):
#     minimo=1[0]
#     for n in 1:
#         if n < minimo:
#             minimo=n
#     return minimo
# print(min(lista))

#crear una funcion que reciba como parametro un nombre y edad  
# de una persona mi funcion debera retornar un diccionario con  los datos 
# luego mostral por terminal  el valor de retorno de mi funcion
# nombre="edith"
# edad=22
# def persona(nombre,edad):
#     return {
#         "nombre":nom,
#         "edad":edad
#     }

# nombre="edith"
# edad=22
# def persona(nombre,edad):
#     return dict(
#         nombre:nom,
#         edad:edad
#     )
# print(persona(nombre,edad))



# #ejercicio con empaquetado
# def suma(*valores):
#     nueva_lisa=list(valores)
#     nueva_lista[0]=10
#     print(nueva_lista)
# suma(2,4,6,3,4,)

 
# ###empaquetado y desempaquetado nominales
# def alumnos(**kwargs):
#     print(kwargs)
# alumnos(nombre="edith",apellido="parinango",edad=20)

#ejercico de lambda

# saludo=lambda:"hola"
# print(saludo())

# saludo=lambda n,a:f"hola, {n} , {a}"
# print(saludo("edith","parinango"))


##crear un programa anonimo que reciba  como parametro una lista de 5 numeros 
#y retorne dos listas una con los numeros pares y otra con numeros impares
# lista=[1,4,6,5,7,9,]
# pares=lambda l:[n for n in lista if n%2==0]
# impares=lambda l:[n for n in lista if n%2!=0]
# print(pares(lista))
# print(impares(lista))

def mensaje(m):
    print(m)
def pedir_nombre():
    nombre=input("ingresa tu nombra")
    return nombre
mensaje(pedir_nombre())