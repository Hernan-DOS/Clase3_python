#Pedir dos números por teclado
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

#Calcular el mayor con operador ternario
mayor = num1 if num1 > num2 else num2

print(f"El número mayor es: {mayor}")
