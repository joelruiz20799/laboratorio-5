# Calculadora básica
def calculadora():
    print("Operaciones disponibles:")
    print("Sumar")
    print("Restar")
    print("Multiplicar")
    print("Dividir")

    operacion = input("Elige una operación (sumar/restar/multi/divi): ")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if operacion == "sumar":
        print(f"Resultado: {num1 + num2}")
    elif operacion == "restar":
        print(f"Resultado: {num1 - num2}")
    elif operacion == "multi":
        print(f"Resultado: {num1 * num2}")
    elif operacion == "divi":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Operación no válida.")

calculadora()