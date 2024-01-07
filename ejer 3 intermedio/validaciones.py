def obtener_numero_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("\nError: Por favor, ingrese un número entero válido.")

def obtener_numero_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("\nError: Por favor, ingrese un número decimal válido.")
