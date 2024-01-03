# main.py

from jugadores_torneo import registrar_jugador, mostrar_registro
from juegos_torneo import registrar_partido
from torneo_torneo import conocer_ganador

if __name__ == "__main__":
    while True:
        print("\nMenú Principal:")
        print("1. Registrar Jugador")
        print("2. Mostrar Registro de Jugadores")
        print("3. Registrar Partido")
        print("4. Conocer Ganador por Categoría")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            id_jugador = input("Ingrese el ID del jugador: ")
            nombre = input("Ingrese el nombre del jugador: ")
            categoria = input("Ingrese la categoría del jugador (Novato/Intermedio/Avanzado): ")
            edad = int(input("Ingrese la edad del jugador: "))
            registrar_jugador(id_jugador, nombre, categoria, edad)

        elif opcion == '2':
            mostrar_registro()

        elif opcion == '3':
            id_jugador1 = input("Ingrese el ID del primer jugador: ")
            id_jugador2 = input("Ingrese el ID del segundo jugador: ")
            resultado_jugador1 = int(input("Ingrese los puntos del primer jugador: "))
            resultado_jugador2 = int(input("Ingrese los puntos del segundo jugador: "))
            registrar_partido(id_jugador1, id_jugador2, resultado_jugador1, resultado_jugador2)

        elif opcion == '4':
            categoria = input("Ingrese la categoría para conocer al ganador: ")
            conocer_ganador(categoria)

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")
