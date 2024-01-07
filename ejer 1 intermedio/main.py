from registro_sismos import registrar_ciudad, registrar_sismo, buscar_sismos, informe_riesgo

def mostrar_menu():
    print("\nMenú:")
    print("1. Registrar Ciudad")
    print("2. Registrar Sismo")
    print("3. Buscar Sismos por Ciudad")
    print("4. Informe de Riesgo")
    print("5. Salir")

def main():
    ciudades = []

    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registrar_ciudad(ciudades)
        elif opcion == 2:
            registrar_sismo(ciudades)
        elif opcion == 3:
            buscar_sismos(ciudades)
        elif opcion == 4:
            informe_riesgo(ciudades)
        elif opcion == 5:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción correcta.")

if __name__ == "__main__":
    main()
