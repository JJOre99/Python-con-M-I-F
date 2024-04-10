# Solicitar saldo al usuario
while True:
    try:
        saldo = float(input("Ingrese el saldo de la cuenta (número positivo): "))
        if saldo >= 0:
            break
        else:
            print("Error: Debe ingresar un número positivo.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

# Calcular el interés correspondiente
if saldo < 10000:
    interes = saldo * 0.03
elif saldo > 810000:
    interes = saldo * 0.04
else:
    interes = 0  # No hay interés en otros casos

# Calcular el saldo final después de un año
saldo_final = saldo + interes

# Mostrar el saldo final
print("El saldo final después de un año es:", saldo_final)
