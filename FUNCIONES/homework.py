#crear un a funcion que reciba por argumentos en el numero y retorne
# #una lista con los numeros pares

# def numero_pares(*args):
#     lista_pares=[]
#     for n in args:
#         if n%2==0:
#             lista_pares.append(n)
#     return lista_pares
# print(numero_pares(2,5,7,8,4,12,5,))

##lista por comprencion

# def numero_pares(*args):
#     return [n for n in args if n%2==0]
# print(numero_pares(2,5,7,8,4,12,5,))

# crear tres funciones para los siguientes casos:
# calcular el numero menor
# calcular el numero mayor
# calcular la suma de todos los numero_pares
# (se le pasara por argumenton numero)
 
def min(*args):
    menor=args[0]
    for n in args:
        if n<menor:
            menor=n
    return suma
def max(*args): 
    mayor=args[0]
    for n in args:
        if n>mayor:
            mayor=n
    return suma
def sum(*args):
    suma=0
    for n in args:
        suma+=n
    return suma 
valores=2,4,6,3,6,8
print(min(*valores))
print(max(*valores))
print(sum(*valores))