def funcion_con_args(*args):
    # Usar operador ternario para verificar
    mensaje = "Se recibieron suficientes argumentos" if len(args) >= 3 else "Error: Se necesitan al menos 3 argumentos"
    return mensaje

# Ejemplo de uso
print(funcion_con_args(1, 2))       # Mostrará error
print(funcion_con_args(1, 2, 3))    # Mostrará mensaje positivo
