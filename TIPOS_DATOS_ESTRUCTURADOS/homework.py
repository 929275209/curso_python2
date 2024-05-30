# Crear la lista de alumnos con nombres, apellidos y edades
lista_alumnos = [
    {"nombre": "Juan", "apellido": "Perez", "edad": 20},
    {"nombre": "Maria", "apellido": "Gomez", "edad": 22},
    {"nombre": "Pedro", "apellido": "Martinez", "edad": 21},
    {"nombre": "Luisa", "apellido": "Garcia", "edad": 23},
    {"nombre": "Carlos", "apellido": "Lopez", "edad": 19}
]

# Insertar al final de la lista los datos de Antonio
antonio = {"nombre": "Antonio", "apellido": "Fernandez", "edad": 25}
lista_alumnos.append(antonio)

# Eliminar de la lista si existe los datos de Abel
abel_index = next((i for i, alumno in enumerate(lista_alumnos) if alumno["nombre"] == "Abel"), None)
if abel_index is not None:
    del lista_alumnos[abel_index]

# Buscar y mostrar el alumno en la posición 4 de la lista
if len(lista_alumnos) >= 4:
    alumno_posicion_4 = lista_alumnos[3]
    print("Alumno en la posición 4 de la lista:", alumno_posicion_4)
else:
    print("No hay suficientes alumnos en la lista.")

# Mostrar la lista de alumnos actualizada
print("\nLista de alumnos actualizada:")
for alumno in lista_alumnos:
    print(alumno)



## 2. crear una lista con tres diccionarios donde tendran ,los datos de sus mascotas (nombre,edad,sexo,raza)
# Crear la lista con tres diccionarios de mascotas
mascotas = [
    {"nombre": "Max", "edad": 5, "sexo": "Macho", "raza": "Labrador"},
    {"nombre": "Luna", "edad": 3, "sexo": "Hembra", "raza": "Golden Retriever"},
    {"nombre": "Bella", "edad": 2, "sexo": "Hembra", "raza": "Poodle"}
]

# Mostrar la lista con los cuatro diccionarios
print("Lista original con los tres registros:")
print(mascotas)

# Editar el tercer registro y cambiar la edad sin modificar la lista original
mascotas_editado = mascotas.copy()  # Copiar la lista original para no modificarla directamente
mascotas_editado[2]["edad"] = 4  # Cambiar la edad del tercer registro

# Mostrar la lista original y luego la lista con el tercer registro editado
print("\nLista original:")
print(mascotas)
print("\nLista con el tercer registro editado:")
print(mascotas_editado)

