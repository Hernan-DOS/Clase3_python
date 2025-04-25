def calcular_promedio(*args):
    # Verificar que hay al menos un número
    if len(args) == 0:
        return "Error: No se ingresaron números"
    
    # Calcular promedio con operador ternario
    promedio = sum(args)/len(args) if len(args) > 0 else 0
    return f"El promedio es: {promedio:.2f}"

# Pedir datos por teclado
print("Ingrese los números separados por espacio:")
numeros = [float(x) for x in input().split()]

# Llamar a la función
print(calcular_promedio(*numeros))
