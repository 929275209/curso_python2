# TIPOS DE DATOS ESTRUCTURADO (TDA- tipos de datos abstractos)
```python
#lista- sus valores o elementos se pueden actualizar
lista=["abel",20,5,2,false,["texto",.2]]

#tupla- sus valoresn o elementos no pueden ser modificados o eliminados
tupla=("abel",10,5,2,False,¨[])

#diccionarios u objetos-los diccionarios almacenan los datos con clave:valor
disccionario={"nombre":"antonio","edad":15,"sexo":False}
```
- [!TIP]
- **OBSERVACION:** Los tipos de datos estructurados pueden almacenar en su interior otros tipos de datos estructurados.
```python
lista_alumnos=[
    (
        "nombre":"abel",
        "edad":20,
    ),(
          "nombre":"abel",
        "edad":20,
    ),(
          "nombre":"abel",
        "edad":20,
    )
```
```python
lista=["abel","anthony","miguel"]
print(lista[1:])
```
```python
lista=["abel","anthony","miguel"]
diccionario={"nombre":"antonio","edad":15}
print(diccionario["nombre"])
```
## Metodos
### 1. convertir texto a lista
```python
#metodo list
texto="hola"
list(texto)
#["h","o","l","a"]

#metodo split
texto="hola como estan"
texto.split(",")
```
### 2. Agregar elementos al final de una lista
```python
##metodo append-
es el metodo que me permite agregar elemntos al
final dde una lista.

lista=["hola"]
lista.append("mundo")
print(lista)

##metodo insert
es el metodoque me permite agregar elementos 
en cualquier ubicacion de mi lista

lista_bnombre=["edith","rut","luz"]
lista_nombres.insert(0,"Antoni")
```
### 3. eliminar elementos de una lista
```python
##metodo pop
al pasarle por parametro un indice este lo 
elimina de la lista.


lista_nombres["edith","rut","luz"]
lista_nombres.pop(0)

##metodo remove
este metodo elimina  por el nombrwe del elemento 
que coincida dentro mi lista.

lista_bnombre=["edith","rut","luz"]
lista_nombres.remove("rut")
```
### 4. buscar un elemento en una lista
```python
##metodo index

lista_nombres["edith","rut","luz"]
indice=lista_nombres.index("rut")
print(lista_nombres[indice])

´pertenencia="edith" in lista_nombres  ##true false
```

### 5. COMPARACION DE LISTAS
Podemos hacer uso de los operadores de comparacion para comparar listas.
```python
compara=[1,2,3]<[1,2,4]
#1 no por que son iguales en ambas listas
#2 no por que son iguales en ambas listas
#3 evalua qu es menor a 4
# entonces la primera lista es menor que la segunda lista
print(compara)
```
### 6. CUIDADO CON LAS COPIAS
### 7. FE DE ERRATAS(actualizar lista)
```python
lista=[1,3,4,5,6,]
lista[0]=2
print(lista)
```

#El director del tecnologico jose maria arguedas
desea actualizar el proceso academico de registro de notas de sus alumnos 
con las siguientes aclaraciones:
-los docemtes podran poner las notas pero no editarlas
solo los coordinadores del programa de estudio podran dar el acceso de edicion de nota
previa peticion del docente encargado
los estudiantes solo podran ver sus notas  y porcentaje de la asistencia esta sera
registrada atraves de un sensor detector en el ingreso del instituto y puerta del aula que se les asignara
la asignacion d aulas  le realizara el secretario academic,si ubiera una observacion por parte de alunmos a su nota o asistencia este lo podra
realizar a traves de la aplicacion en observacion que sera enviado a su docente y coordinador y programa de estudio

#yo como docente

#puedo hacer la solicitud la edicion de notas

#para correjir las  notas las notas erroneas

## LISTAS Y DICIONARIOS POR COMPRENCION
es una tecnica pythonica que nos permite crear listas y diccionarios bubles y deciciones
> [!NOTE] 
> 
> ***VLC*** value loop condicion - valor bucle condicion
```python
#lista por comprencion
texto="1,4,8,9,6"
nueva_lista=[int(n) for n in texto.split(",") if int (n)%2==0]
print(nueva_lista

```
```python
#lista por comprencion
lista_amigos=["abel","edith","antoni","rut"]
diccionario={amigo:len(amigo) for amigo in lista_amigos}
print(diccionario)
```





