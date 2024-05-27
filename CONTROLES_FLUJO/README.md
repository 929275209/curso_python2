# CONTROLES DE FLUJO
todos los programas trabajan de instrucciones ordenadas.
existen maneras de romper con el fujo normal de los programs creando  `bifurcaciones` o creando `repeticion`.
<<<<<<< HEAD
## DESICIONES
## >la sentencia if
la sentencia de decicion de python es `if` en su escritura debemos añadir una **expresion de comparacion** terminando con `:` al final de la linia.

## deciciones
La sentencia de decicion de python es `if` en su escritura debemos añadir una **expresion de comparacion** terminando con `:` al final de la linia.

> ejemplo:
else-elif
```
edad:int=int("escribe tu edad: ")
if edad>18:
    print("eres mayor de edad)
else:
("eres menor de edad)
```
>ejemplo:
if
```python
if true:
    print("es verdad") 
```


## CICLOS
Son los controles de flujo que repiten codigo y sintaxis en la siguiente.
> ejemplo:
```python
```
## >for
Es una secuencia de elementos como una lista, un diccionario o una cadena de texto.
(n) es una variable
> ejemplo: for
```python
for n in range(1,11):
    print(n)
    
```
## rangue
oraciones pequeño(es mas rapido y consume menos)
## in
oraciones medianas(consume mas)
## enumerate
oraciones medinas y grandes consume menos y ejcucion  rapida

## >WHILE
se usa para repetir un bloque de codigo o instrucciones mientras se cumpla una condicion especifica.(intervencion de un tercero para que termine la ejecucion)
>ejemplo: **while**
```python

while condicion:
    eval=input("desea continuar[S/N]):
    if eval=="S":
        print("continuas en el bucle"):
        continue
    else:
        print("se termino el programa)
        condicion=false
        break
```             
```python
while contador<=5:
    print(contador)
    contador+=1
    print(f"el valor final {contador}")
```
```python
nombre="jose"
nombre.opper()#convierte el texto en mayuscula

nombre="JOSE"
nombre.lower()#convierte el texto en minuscula
```