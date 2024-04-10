import math

def obtener_numero():
    while True:
        try:
            numero = float(input("Por favor, introduce un número positivo: "))
            if numero >= 0:
                return numero
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido.")

def calcular_raiz_cuadrada(numero):
    return math.sqrt(numero)

def main():
    numero = obtener_numero()
    raiz_cuadrada = calcular_raiz_cuadrada(numero)
    print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")

if __name__ == "__main__":
    main()
