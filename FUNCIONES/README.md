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
para definir una funcion en python primero utlizaremos la palabra reservada **_def_** seguida por el **_nombre_** de la funcion . A continuacion especificaremos  los **_parametros_** con **_( )_** si es una funcion sin parametros, **_(a)_** si es una funcion con parametros, si se tuviera mas de un paramtro iran separados por **_,_** , finalizaremos la linia con **_:_**, en la siguiente linia  sin olvidar el identado, comenzara el **_cuerpo_** de la funcion(microprograma) que puede contener 1 o mas sentencias, finalmente debera **_retornar_** con la palabra reservada **_return_**
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
```python
def uno()]:
    return 1
uno()
```
>[!WARNING]
No confundir **print( )** con **return**, el valor retornado por **return** nos permite usarlo

### RETORNAR MULTIPLES VALORES
El secreto es hacerlo mediante un tipo de dato estructurado.
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