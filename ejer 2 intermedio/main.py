# main.py
from facturacion import (
    obtener_consumos_por_dependencia,
    obtener_factor_emision_energia,
    obtener_periodo_facturacion
)
from calculos_emisiones import (
    calcular_emisiones_total
)

def mostrar_menu():
    print("\nMenú:")
    print("1. Registrar Dependencia")
    print("2. Registrar Consumo por Dependencia")
    print("3. Ver CO2 Producido")
    print("4. Dependencia que Produce Mayor CO2")
    print("5. Salir")

def main():
    consumos_por_dependencia = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consumos_por_dependencia.append(obtener_consumos_por_dependencia())
        elif opcion == "2":
            if not consumos_por_dependencia:
                consumos_por_dependencia = obtener_consumos_por_dependencia()
            else:
                consumos_por_dependencia.extend(obtener_consumos_por_dependencia())
        elif opcion == "3":
            factor_emision_energia = obtener_factor_emision_energia()
            total_emisiones = calcular_emisiones_total(consumos_por_dependencia, factor_emision_energia)
            print(f"CO2 total producido: {total_emisiones} tCO2eq")
        elif opcion == "4":
            if not consumos_por_dependencia:
                print("Error: Aún no se han registrado consumos por dependencia.")
            else:
                max_emisiones = max((calcular_emisiones_total(consumos, obtener_factor_emision_energia()) for consumos in consumos_por_dependencia), default=0)
                print(f"La dependencia que produce mayor CO2 emite: {max_emisiones} tCO2eq")
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Error: Opción no válida. Por favor, seleccione una opción correcta.")

if __name__ == "__main__":
    main()
