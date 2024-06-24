# FUNCIONES
Matematicamente ena funcion es una operacion que toma uno o dos valores llamados **_ARGUMENTOS_** y produce un valor denominado **_RESULTADO_**
>[!NOTE]
Todos los lenguajes de programacion tienen funciones incorporadas(**_funciones internas_**),funciones creadas por el usuario(**_funciones externas_**)

En programacion una funcion es un sub-programa, es una estructura que nos permite agrupar codigo y sus principlaes obejetivos es/son:
- No repetir fracmentos de codigo.
- Reutilizar el codigo en distintos escenarios.
## ESTRUCTURA DE UNA FUNCION

- Una funcion viene **_definida_** por un **_nombre_** sua **_parametros_** y su valor de **_retorno_**

- Una vez creada la funcion podremos solicitar su ejecucion **_invocando_** la funcion por su **_nombre_**.

## DEFINIR UNA FUNCION EN PYTHON
para definir una funcion en python primero utlizaremos la palabra reservada `def` seguida por el `nombre`de la funcion . A continuacion especificaremos  los `parametros` con `()`si es una funcion sin parametros, `(a)` si es una funcion con parametros, si se tuviera mas de un paramtro iran separados por **_,_** , finalizaremos la linia con **_:_**, en la siguiente linia  sin olvidar el identado, comenzara el **_cuerpo_** de la funcion(microprograma) que puede contener 1 o mas sentencias, finalmente debera **_retornar_** con la palabra reservada **_return_**
>[!TIP]
Como retorno tambien se puede utilizar la **_funcion interna_**, **_print()_**, para depuracion de codigo no es recomendable usarlo en produccion.

**_PRINT_** DENTRO DE UNA FUNCION ES UNA HERRAMIENTA QUE SE UTILIZXAR PARA CMOMPROBAR QUE UNA FUNCUION ESTE TRABAJANDO CORRECTO.

**EJEMPLO**
``` python
def saludo():
    saludo="hola"
    saludo_dos="como estas"
    return saludo+saludo_dos
    saludo()
```
```python
def saludo():
    saludo="hola"
    saludo_dos="como estas"
    return f"(saludo), (saludo_dos)"
    print(saludo)
```

### INVOCAR UNA FUNCION
Para invocar(o llamar ,ejecutar una funcion solo tendremos que escribir si el **_nombre_** de la funcion seguido por **( )** parentesis.
```python
def saludo():
    print("hola")
#invocando la funcion
saludo()
```
### RETORNAR UNA FUNCION

las funciones pueden retornar (o devolver) un valor.

>ejemplo
```python
def uno():
    return 1
uno()
```
>[!WARNING]
No confundir **print( )** con **return**, el valor retornado por **return** nos permite usarlo

### RETORNAR MULTIPLES VALORES
El secreto es hacerlo mediante un tipo de dato estructurado.
>ejemplo
```python
#tupla
def varios():
    return 2,3,4
    varios()
```
```python
#lista
def nombre():
    return{"nombre":"jose","edad":45}
nombre()

```
**return**- tipo de 
       tipo de dato estrcuturado 

 **print**- mensaje  

 ### PARAMETROS Y ARGUMENTOS 
 Si una funcion no dispusiera d valores de entrada estaria limityada en su actuacion, es por ello que los **_parametros*_** nos permiten variar los datos que consumen una funcion para obtener distintos resultados 
 ejemplo
 crear una funcon que recive un valor umerico y devuelve su raiz cuadrada
 >ejemplo
 ```python
def sqrt(valor):
    return valor**(1/2)
#NOTA: En este caso el valor 4 es un argumento de la funcion
    sqrt(4)
 ```   
 cuando llamamos a una funcion con **_argumentos_** los valores de estos argumentos  se copia en su correspondiente **_parametro_** dentro de la funcion
 >ejemplo
 ```python
def suma(a,b,c):
    return a+b+c
suma(4,5,6)
 ```
 ### ARGUMENTOS NOMINALES
 En esta aproxnimacion los argumentos no son copiados en  orden, si no que, **_se asigna por nombre a cada parametro_** ello nos permiten evitar el problema de conocer o recuordar cual es el orden de los parametros en la definicion dela funcion , para utilizar basta  realizar una asignacion dse cada argumento  en la propia llamda a la funcion.
 >ejemplo
 ```python
def build_cpu(familia,num_core,,frecuencia):
    print(f"""
        la cpu es de la familia {familia},
        con {num_core} cores y con una
        frecuencia de {frecuencia}
    """)
    #haciendo uso de argumentos nominales
build_cpu(num_core=4,familia="intel",frecuencia=2.7)
 ```
### ARGUMENTOS POSICIONALES
 Los argumentos  son copiados en un oreden especifico, en este caso debemos conocer o recordar cual es el orden de los parametros.
 >ejemplo
 ```python
def build_cpu(familia,num_core,,frecuencia):
    print(f"""
        la cpu es de la familia {familia},
        con {num_core} cores y con una
        frecuencia de {frecuencia}
    """)
    #haciendo uso de argumentos nominales
build_cpu("intel",4,2,7)
 ```
### PARAMETROS POR DEFECTO
Es posible especificar **_valores por defecto_** con los parametros de una funcion, en el caso que no se proporcione un valor al argumento en la llamada/ojecucion el parametro correspondiente tomaran el valor definid por defecto 
>ejemplo
```python
def alumnos(nombre,apellido,estado="aprobado"):

alumnos("rut","castillo")
alumnos("edith","parinango")
```
### DESEMPAQUETADO/EMPAQUETADO DE ARGUMENTOS(tarea)
### Empaquetado de ARGUMENTOS 
El empaquetado de argumentos ocurre cuando se pasa un número variable de argumentos a una función y estos se agrupan en una sola variable, generalmente una tupla. Esto se realiza precediendo el nombre del parámetro con un asterisco (*). 
> ejemplo
```python
def sumar(*args):
    total = 0
    for num in args:
        total += num
    return total

resultado = sumar(1, 2, 3, 4, 5) 
# Empaquetado de argumentos
print(resultado) 
 # Salida: 15
```
### Desempaquetado de ARGUMENTOS
El desempaquetado de argumentos es cuando se pasa una estructura de datos, como una tupla o una lista, a una función y se desempaqueta en argumentos individuales. Esto se realiza precediendo el nombre de la estructura de datos con un asterisco (*).
> ejemplo
```python
def saludar(nombre, apellido):
    print(f"Hola {nombre} {apellido}!")

datos = ("Juan", "Pérez")
saludar(*datos)  
# Desempaquetado de argumentos

```
### empaquetado y desempaquetado NOMINALES
>ejemplo
```python
def alumnos(**kwargs):
    print(kwargs)
alumnos(nombre="edith",apellido="parinango",edad=20)
```
>ejemplo
```python
#reemplazando nombre
def alumnos(**kwargs):
    kwargs["nombre"]="abel"
    print(kwargs)
alumnos(nombre="edith",apellido="parinango",edad=20)
```


##  FUNCIONES INTERNAS DE PYTHON(tarea)

- `print()` Utilizado para imprimir texto o variables en la consola. 
- `len()`Retorna la longitud de un objeto iterable como una lista, tupla, cadena, etc.
- `type()` Retorna el tipo de un objeto.
- `input()`Lee la entrada del usuario desde la consola.
- `range`Genera una secuencia de números.
- `open`Abre un archivo en un modo específico.
- `str, int, float`Convierten un objeto a cadena, entero o flotante, respectivamente.
- `sum`Retorna la suma de todos los elementos en un iterable.
- `max, min`Retorna el valor máximo o mínimo de un iterable.
- `sorted`Retorna una lista ordenada a partir de un iterable.
- `abs`Retorna el valor absoluto de un número.
- `range`Retorna una secuencia inmutable de números.

## TIPOS DE FUNCIONES

#### -FUNCIONES ANONIMAS(funciones lambda)
Son funciones sin nombre que se puedan utlizarde forma anonima en un programa
```python
lambda:"hola"
#normal
def saludo():
    return "hola"
```
#### -FUNCIONES CLOSURE
Es una funcion que hace referencia a variables de su ambito externo en el mmento de su definicion
```python

```
#### -FUNCIONES CALLBACK
```python

```
#### -PROGRAMACION FUNCIONAL
La programcion funcional no requiere que sepas como se desarrolla y ejecuta el procesamiento de la informacion
```python
lista=[3,4,6,7,2]
def num_minimo(1):
    minimo=1[0]
    for n in 1:
        if n < minimo:
            minimo=n
    return minimo
#programacion funcional
min(lista)
```
#### 🎈averiguar sobre map(), filter(), reduce()
### `map()`
 toma una funcion y un iterable como argumentos y aplica la funcion a cada elemento del iterable, devolviendo un nuevo iterable con los resultados.
`sintaxis.- map(funcion,iterable)`

### `filter()` 
toma una funcion que devuelve un valor booleano(true o false)y un iterable, y devuelve un nuevo iterable con los elmentos del iterable para los cuales la funcion devuelve true.
`sintaxis.- filter(funcion,iterable)`

### `reduce()`
 aplica una funcion de dos argumentos de forma acumulativa a los elemenmtos de un iterable, reduciendolos a un solo valor.
`sintaxis.- reduce(funcion,iterable)`