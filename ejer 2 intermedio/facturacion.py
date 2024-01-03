# facturacion.py

def obtener_float_input(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico válido.")

def obtener_consumo_electricidad():
    return obtener_float_input("Ingrese el consumo de electricidad en kilovatios-hora (kWh): ")

def obtener_kilometros_recorridos():
    return obtener_float_input("Ingrese la cantidad de kilómetros recorridos: ")

def obtener_factor_emision_electricidad():
    return obtener_float_input("Ingrese el factor de emisión de electricidad: ")

def obtener_factor_emision_transporte():
    return obtener_float_input("Ingrese el factor de emisión del transporte: ")

def obtener_factor_emision_energia():
    return obtener_float_input("Ingrese el factor de emisión de energía: ")

def obtener_periodo_facturacion():
    while True:
        periodo = input("Ingrese el periodo de facturación (ej. mensual, bimestral): ").lower()
        if periodo in ["mensual", "bimestral"]:
            return periodo
        else:
            print("Error: Por favor, ingrese 'mensual' o 'bimestral'.")

def obtener_consumos_por_dependencia():
    while True:
        try:
            n_dependencias = int(input("Ingrese el número de dependencias: "))
            if n_dependencias > 0:
                break
            else:
                print("Error: El número de dependencias debe ser mayor que cero.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

    consumos = []

    for i in range(1, n_dependencias + 1):
        consumo = obtener_float_input(f"Ingrese el consumo de la dependencia {i} en kWh: ")
        consumos.append(consumo)

    return consumos
