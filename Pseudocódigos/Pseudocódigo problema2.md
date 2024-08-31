Inicio

    Pedir altitud_inicial
    Pedir coeficiente_arrastre
    Pedir altitud_minima_seguridad
    
    altitud_actual = altitud_inicial
    coeficiente_arrastre_actual = coeficiente_arrastre
    numero_orbitas = 0
    incremento_coeficiente_arrastre = 0.0001
    umbral_estabilizacion = 0.001

    mientras altitud_actual > altitud_minima_seguridad y altitud_perdida > umbral_estabilizacion
        altitud_perdida = coeficiente_arrastre_actual * altitud_actual
        altitud_actual = altitud_actual - altitud_perdida
        coeficiente_arrastre_actual = coeficiente_arrastre_actual + incremento_coeficiente_arrastre
        numero_orbitas = numero_orbitas + 1
        
        si altitud_perdida <= umbral_estabilizacion
            romper
    
    si altitud_actual <= altitud_minima_seguridad
        mostrar "El satélite ha reingresado en la atmósfera terrestre después de", numero_orbitas, "órbitas."
    sino
        mostrar "El satélite se ha estabilizado en una órbita a una altitud de", altitud_actual, "kilómetros después de", numero_orbitas, "órbitas."
Fin

