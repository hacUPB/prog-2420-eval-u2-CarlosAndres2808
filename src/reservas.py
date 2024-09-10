# Información del usuario

Titulo = input("Ingrese su título (Sr. o Sra.):")
Nombre = input ("Ingrese su nombre:")
Apellido = input ("Ingrese su apellido:")
print(f"{Titulo}, {Nombre}, {Apellido}, ¡Bienvenido a FastFast Airlines!")

# Selección del vuelo

origen = input("Opciones: Medellín, Bogotá, Cartagena:")
print("Seleccione su ciudad de origen:")
destino = input("Opciones: Medellín, Bogotá, Cartagena:")
print("Seleccione su ciudad de destino:")
día_semana = input("Ingrese el día de la semana en el que desea viajar:(Lunes, Martes, Miercoles, Jueves, Viernes, Sábado, Domingo:) ")
día_mes = input("Ingrese el día del mes (1-30):")

print(f"Origen: {origen}")
print(f"Destino: {destino}")

# Precio del billete
Precio = 0
def calcular_precio(origen, destino, día_semana):

    distancia = (origen, destino) or (destino, origen)
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
    
print(f"Precio del boleto: ${calcular_precio}")

# Distancias entre las ciudades

Distancia = 0 

(Medellín, Bogotá)= 240
(Medellín,Cartegana)= 461
(Bogotá,Cartagena)= 657

# Asignación de asiento

def asignar_asiento(preferencia):
    número_asiento = random.randint(1, 29)
    if preferencia == 'pasillo':
        return f"{número_asiento} C"
    elif preferencia == 'ventana':
        return f"{número_asiento} A"
    else: 
        return f"{número_asiento} B"

print(f"Asiento asignado: {asignar_asiento}")

        
