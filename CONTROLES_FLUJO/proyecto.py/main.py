#  SISTEMA DE CONTROL DE GRASS SINTETICO

# El usuario tiene un gras el cual administra de manera manual, el usuario necesita que se automatize el proceso de la reserva y pago del alquiler, para lo cual solicita automatizar los siguientes casos de uso.

# 1.- el usuario podra ver lista de horarios disponibles.
# 2.- el usuario podra reservar en uno de los horarios disponibles.
# 3.- el usuario podra pagar por el alquiler de la reserva realizada.
# 4.- el usuario podra verificar su alquiler el cual le muestra los detalles como la fecha , hora y costo del alquiler que realizo.

horarios:list=[] #creando una lista vacia:
horarios_disponibles=f"""

 _______________HORARIOS_DISPONIBLES__________________

 1.- Lunes 14 (13:00 pm a 15:00 pm)
 2.- Miercoles 16 (15:00 pm a 17:00 pm)
 3.- Viernes 18 (13:00 pm a 15:00 pm)

 _____________________________________________________

 """

while True:
    print(horarios_disponibles)
    opcion=int(input("Ingrese el horario que desee: "))
    if opcion== int("1"):
        costo_1=50 
        print(f"Empieza el Lunes 14 a las 13:00pm hasta las 15:00 pm, y el costo es  {costo_1} soles")
        break
    elif opcion== int("2"):
        costo_2=60
        print (f"Empieza el Lunes 14 a las 13:00pm hasta las 15:00 pm, y el costo es  {costo_2} soles")
    elif opcion==int ("3"):
        costo_3=70
        print (f"Empieza el Lunes 14 a las 13:00pm hasta las 15:00 pm, y el costo es  {costo_3} soles")
    break










