# texto="hola"
# lista_texto=list(texto)
# lista2=[e for e in texto]
# print(lista2)

#SPLIT
# texto_largo="hola como estan vienvenidos al salon"
# nuevo_texto=texto_largo[16:]
# nueva_lista=nuevo_texto.split(" ")
# print(nueva_lista)

# texto_largo="loquitas_.mp4"
# nuevo_texto=texto_largo.split(" ")
# print(",".join(nuevo_texto))
# #join-es el metodo para unirelementos en un solo texto

# numeros=[1,2,3]
# print(id(numeros))
# otra_lista=numeros
# print(id(otra_lista))


#DATOS  ESTRUCTURADOS

# lista_original=[1,2,3,4]
# copia_lista=lista_original

# lista_original[-1]=15
# print(copia_lista)


#CREAR UN PROGRAMA  QUE RECIBA UNA LISTA DESORDENADA Y  MUESTRE POR
# TERMINAL LA LISTA ORDENA Y LA LISTA PREVIA A SER ORDENADA
#1
# lista=[2,5,1,4,3]
# lista.sort()
# print(lista)

# #2
# lista=[2,5,1,4,3]
# copia_lista=lista.copy()
# copia_lista.sort()
# print(lista)
# print(copia_lista)

#crear una lista de numeros enteros del sigguiente texto

# texto="1,4,8,9,6"
# convertir=texto.split(",")
# print(convertir)

# texto="1,4,8,9,6"
# nueva_lista=[]
# for n in texto.split(","):
#     nueva_lista.append(int(n))
#     print(nueva_lista)

###ejercicio aplicando "vlc"

# texto="1,4,8,9,6"
# nueva_lista=[int(n) for n in texto.split(",") if int (n)%2==0]
# print(nueva_lista)


#diccionarios por comprencion

# lista_amigos=["abel","edith","antoni","rut"]
# diccionario=()
# for _,v in enumerate(lista_amigos):
#     diccionario[v]=len(v)
# print(diccionario)

###ejercicio aplicando "vlc"

lista_amigos=["abel","edith","antoni","rut"]
diccionario={amigo:len(amigo) for amigo in lista_amigos}
print(diccionario)