Inicio

    Escribir: Información_usuario
    Pedir al usuario que ingrese su título (Sr. o Sra.)
    Pedir al usuario que ingrese su nombre
    Pedir al usuario que ingrese su apellido
    
    Mostrar saludo personalizado:
        saludo = "titulo nombre apellido, ¡Bienvenido a FastFast Airlines!"
        Mostrar saludo

    Escribir: Vuelo_seleccionado
    Mostrar opciones de ciudades (Medellín, Bogotá, Cartagena)
    Pedir al usuario que seleccione la ciudad de origen
    Pedir al usuario que seleccione la ciudad de destino
    Pedir al usuario que ingrese el día de la semana y el mes en el que desea viajar (entre 1 y 30)
    
    Calcular la distancia entre origen y destino
    Si (origen = "Medellín" y destino = "Bogotá") entonces
        distancia = 240
    Sino si (origen = "Medellín" y destino = "Cartagena") entonces
        distancia = 461
    Sino si (origen = "Bogotá" y destino = "Cartagena") entonces
        distancia = 657
    Sino
        distancia = 0 
    Imprimir Error, ciudad no válida
    
    Calcular el precio del billete
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

    Escribir asiento_asignado
    Pedir al usuario que indique su preferencia de asiento (pasillo, ventana, sin preferencia)
    
    Definir el tipo de asiento basado en la preferencia
    Si (preferencia = "pasillo") entonces
        tipo_asiento = "C"
    Sino si (preferencia = "ventana") entonces
        tipo_asiento = "A"
    Sino
        tipo_asiento = "B"
    
    Definir aleatoriamente un número de asiento entre 1 y 29
    numero_asiento = GenerarNúmeroAleatorio(1, 29)
    
    Definir el asiento asignado combinando el número y el tipo de asiento
    asiento_asignado = numero_asiento + tipo_asiento

    Escribir: Salida
    Mostrar nombre completo del usuario
    Mostrar origen
    Mostrar destino
    Mostrar fecha de vuelo (día de la semana y día del mes)
    Mostrar precio del boleto
    Mostrar asiento asignado
Fin si

Fin
