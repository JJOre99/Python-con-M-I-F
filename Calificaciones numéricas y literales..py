# Función para convertir calificación numérica a literal
def calificacion_literal(calificacion):
    if calificacion >= 90:
        return "A - Excelente"
    elif calificacion >= 80:
        return "B - Muy Bueno"
    elif calificacion >= 70:
        return "C - Bueno"
    elif calificacion >= 60:
        return "D - Aceptable"
    else:
        return "F - Insuficiente"

# Solicitar calificación numérica al usuario
calificacion_numerica = float(input("Ingresa tu calificación numérica: "))

# Imprimir calificación literal
print("Tu calificación es:", calificacion_literal(calificacion_numerica))
