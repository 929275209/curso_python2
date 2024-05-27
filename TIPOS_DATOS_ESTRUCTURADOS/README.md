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




