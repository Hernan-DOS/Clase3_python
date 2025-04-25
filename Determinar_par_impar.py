# Pedir número por teclado
numero = int(input("Ingrese un número: "))

# Determinar par/impar con operador ternario
resultado = "par" if numero % 2 == 0 else "impar"

print(f"El número {numero} es {resultado}")
