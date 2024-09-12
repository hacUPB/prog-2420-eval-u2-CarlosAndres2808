

# Información del usuario

import random


Titulo = input("Ingrese su título (Sr. o Sra.):")
Nombre = input ("Ingrese su nombre:")
Apellido = input ("Ingrese su apellido:")
print(f"{Titulo}, {Nombre}, {Apellido}, ¡Bienvenido a FastFast Airlines!")

# Selección del vuelo

origen = input("Ingresa tu origen (Medellín, Bogotá, Cartagena): ")
destino = input("Ingresa tu destino (Medellín, Bogotá, Cartagena): ")
día_semana = input("Ingrese el día de la semana (por ejemplo, lunes): ")
día_mes = input("Introduzca el día del mes (1-30): ")

origen_destino = {
    "Medellín,Bogotá" : 240,
    "Bogotá,Medellín" : 240,
    "Medellín,Cartagena": 461,
    "Cartagena,Medellín": 461,
    "Bogotá,Cartagena": 657,
    "Cartagena,Bogotá": 657,
}

# Precio del billete
Precio = 0
def calcular_precio(origen, destino, día_semana):

    distancia = origen_destino[f"{origen},{destino}"]
    if distancia < 400:
       if día_semana in ['lunes', 'martes', 'miércoles', 'jueves']:
           return 79900
       else:
           return 119900
    if distancia >= 400:
        if día_semana in ['lunes', 'martes', 'miércoles', 'jueves']:
            return 156900
        else: 
            return 213000
    
# Asignación de asiento
preferencia = input("Asiento de preferencia (pasillo,ventana,indiferente): ")
def asignar_asiento(preferencia):
    número_asiento = random.randint(1, 29)
    if preferencia == 'pasillo':
        return f"{número_asiento}C"
    elif preferencia == 'ventana':
        return f"{número_asiento}A"
    else: 
        return f"{número_asiento}B"

print(f"Tu vuelo de {origen} a {destino} del {día_semana} {día_mes} de abril está reservado.")
print(f"Precio del boleto: ${calcular_precio(origen, destino, día_semana)}")
print(f"Tu asiento es: {asignar_asiento(preferencia)} ") 