Inicio

    // Paso 1: Información del usuario
    Solicitar al usuario que ingrese su título (Sr. o Sra.)
    Solicitar al usuario que ingrese su nombre
    Solicitar al usuario que ingrese su apellido
    
    Mostrar saludo personalizado:
        saludo = "titulo nombre apellido, ¡Bienvenido a FastFast Airlines!"
        Mostrar saludo

    // Paso 2: Selección de vuelo
    Mostrar opciones de ciudades (Medellín, Bogotá, Cartagena)
    Solicitar al usuario que seleccione la ciudad de origen
    Solicitar al usuario que seleccione la ciudad de destino
    Solicitar al usuario que ingrese el día de la semana en el que desea viajar
    Solicitar al usuario que ingrese el día del mes (entre 1 y 30)
    
    // Determinar la distancia entre origen y destino
    Si (origen = "Medellín" y destino = "Bogotá") entonces
        distancia = 240
    Sino si (origen = "Medellín" y destino = "Cartagena") entonces
        distancia = 461
    Sino si (origen = "Bogotá" y destino = "Cartagena") entonces
        distancia = 657
    Sino
        distancia = 0 // Error, ciudad no válida
    
    // Calcular el precio del billete
    Si distancia < 400 entonces
        Si (día de la semana es lunes a jueves) entonces
            precio = 79900
        Sino
            precio = 119900
    Sino
        Si (día de la semana es lunes a jueves) entonces
            precio = 156900
        Sino
            precio = 213000

    // Paso 3: Asignación de asiento
    Solicitar al usuario que indique su preferencia de asiento (pasillo, ventana, sin preferencia)
    
    // Asignar el tipo de asiento basado en la preferencia
    Si (preferencia = "pasillo") entonces
        tipo_asiento = "C"
    Sino si (preferencia = "ventana") entonces
        tipo_asiento = "A"
    Sino
        tipo_asiento = "B"
    
    // Seleccionar aleatoriamente un número de asiento entre 1 y 29
    numero_asiento = GenerarNúmeroAleatorio(1, 29)
    
    // Crear el asiento asignado combinando el número y el tipo de asiento
    asiento_asignado = numero_asiento + tipo_asiento

    // Paso 4: Salida
    Mostrar nombre completo del usuario
    Mostrar origen
    Mostrar destino
    Mostrar fecha de vuelo (día de la semana y día del mes)
    Mostrar precio del boleto
    Mostrar asiento asignado

Fin
