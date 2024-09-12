
    
    # satelite.py
def simular_desintegracion_orbital():

    # Solicitar datos al usuario
    altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en km):"))
    coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (por ejemplo, 0.01):"))
    altitud_minima = float(input("Ingrese la altitud mínima de seguridad (en km):"))
    
    # Iniciar variables
    altitud_actual = altitud_inicial
    orbita = 0
    
    
    # Simulación desceso órbita
    while altitud_actual > altitud_minima:
        # Calcular la pérdida de altitud en esta órbita
        altitud_perdida = coeficiente_arrastre * altitud_actual
        altitud_actual -= altitud_perdida
        orbita += 1
        
        # Aumentar el coeficiente de arrastre para simular mayor resistencia
        coeficiente_arrastre += 0.0001
        
        print(f"Órbita {orbita}: Altitud actual = {altitud_actual} km, Coeficiente de arrastre = {coeficiente_arrastre}")
    # Si el bucle termina, el satélite ha reingresado en la atmósfera
    print(f"El satélite ha reingresado en la atmósfera terrestre después de {orbita} órbitas.")
    print(f"Altitud final: {altitud_actual:} km.")

# Ejecutar la simulación
simular_desintegracion_orbital()

