def buscar_palabra(*args):
    # args[0] es la palabra a buscar, args[1:] es la lista
    palabra = args[0]
    lista = args[1:]
    
    # Usar operador ternario para verificar si está en la lista
    resultado = f"'{palabra}' está en la lista" if palabra in lista else f"'{palabra}' no está en la lista"
    return resultado

# Pedir datos por teclado
palabra_buscar = input("Ingrese la palabra a buscar: ")
print("Ingrese los elementos de la lista (separados por espacio):")
elementos = input().split()

# Llamar a la función
print(buscar_palabra(palabra_buscar, *elementos))
