
# #primer ejemplo de if estructurado
# edad:int=int(input("escribe tu edad: "))
# if edad>18:
#     print("eres mayor de edad")
# else:
#     print("eres menor de edad")

# #segundo ejemplo de if almacenado en variable
# edad_dos:int=int(input("escribe tu edad: "))
# respuesta:str="eres mayor" if edad_dos>18 else "eres menor"
# print(respuesta)




# #crear un programa que imprima las 5 vocales
# vocales:str="aeiou"
# print(vocales[1])
# print(vocales[2])
# print(vocales[3])
# print(vocales[4])
# print(vocales[5])

# vocales:str="aeiou"
# for n in range(o,5):
#     print(vocales[n])



# #crear un programa que que me muestre los 8 primeros numeros pares
# contador=0
# for n in range (1,17):
#     if n%2==0:
#      contador+=1
#     print(f"{n} es par numero {contador}")




# #crear programa al usario escribir una oracion y mostrar por terminal
# #cantidad de vocales "a" que tiene esa oracion.

# oracion:str=input("ingrese una oracion: ")
# contador:int=0
# for n in range (0,len(oracion)):
#     if oracion[n]=="a":
#         contador=contador+1
# print(f"la cantidad de letras a que tengo es {contador}")


# #segunda manera
# for i,l in enumerate("aeiou"):
#     print(f"el indice{i}la letra es{l}")
# print(f"la cantidad de letra a que tengo es {contador}")


#crear un programa que me muestre la cantidad de comas y me muestre sus indices 
# oracion:str=input("ingrese una oracion: ")
# contador=0
# for indice,letra in enumerate(oracion):
#      if letra==",":
#         print(f"su indice es {indice}")
#         contador+=1
# print(f"la cantidad de comas es {contador}")


#crear un programaque pregunte al usuario su edady mueste por pantalla todos 
#los años #que ah cumplido des 1 hata su edad actual
# edad=int(input("ingrese su edad"))
# for i in range(1, edad+1):
#     print(f"has cumplido ", i, "años")


#crear un programa qu me pida elnombre de tres personas 
#y guarde en una variable la ultima letra de sus nombres
#mostrar por pantalla la variable global con las tres ultimas letras del 
#nombre de cada perona
# nombre1:str=input("ingrese el primer nombre")
# nombre2:str=input("ingrese el segundo nombre")
# nombre3:str=input("ingrseerl tercer nombre")  
# ultima_letra1=nombre1[-1] 
# ultima_letra2=nombre2[-1]
# ultima_letra3=nombre3[-1]
# print("las ultimas letras de los nombres son:", ultima_letra1,
#        ultima_letra2, ultima_letra3)

#segunda manera
# ultima_letra:str=""
# for n in range(3):
#     nombre:str=input("ingrese tu nombre")
#     ultima_letra+=nombre[-1]
#     last_letter:str=nombre[-1]
#     ultima_letra+=last_letter
#     print(ultima_letra)

 #crear un programa que muestree por terminal la siguiente figura
 #a
 #ee
 #iii
 #oooo
 #uuuuu

# altura=int(input("ingrese la altura del triangulo"))
# for i in range(1,altura +1):
#   print("a")
#  

#crear un programa que me pida la cantidad de notas que se debe 
#registrar luego pedira las notas e imprima el promedio
cantidad_notas=int(input("ingrese las notas: "))
suma_notas=0
contador=0
                         



    



