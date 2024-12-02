# Condicional para par o impar
numero = int(input("Introduce un numero: "))

if numero % 2 == 0:
    print("El numero es par.")
else:
    print("El numero es impar.")

# Bucle for para imprimir cuadrados
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(f"El cuadrado de {numero} es {numero ** 2}.")

# Bucle while con condición
while True:
    respuesta = input("¿Quieres continuar? (si/no): ").lower()
    if respuesta == "no":
        print("¡Hasta luego!")
        break
    elif respuesta == "si":
        print("¡Continuamos!")
    else:
        print("Por favor, responde con 'si' o 'no'.")
