import math

def grados_a_radianes(grados):
    return grados * (math.pi / 180)

def radianes_a_grados(radianes):
    return radianes * (180 / math.pi)

def main():
    while True:
        try:
            opcion = int(input("Seleccione la conversión que desea realizar:\n1. De hexagesimales a radianes\n2. De radianes a hexagesimales\nIngrese el número de la opción: "))
            if opcion not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Error: Por favor, ingrese 1 o 2 para seleccionar la conversión.")

    if opcion == 1:
        while True:
            try:
                grados = float(input("Ingrese los grados hexagesimales a convertir a radianes: "))
                radianes = grados_a_radianes(grados)
                print(f"{grados} grados hexagesimales son aproximadamente {radianes} radianes.")
                break
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido para los grados.")
    else:
        while True:
            try:
                radianes = float(input("Ingrese los radianes a convertir a grados hexagesimales: "))
                grados = radianes_a_grados(radianes)
                print(f"{radianes} radianes son aproximadamente {grados} grados hexagesimales.")
                break
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido para los radianes.")

if __name__ == "__main__":
    main()