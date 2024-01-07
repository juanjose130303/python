from jugadores_torneo import jugadores, actualizar_estadisticas_partido, obtener_ganador_por_categoria

def registrar_partido(id_jugador1, id_jugador2, resultado_jugador1, resultado_jugador2):
    if id_jugador1 not in jugadores or id_jugador2 not in jugadores:
        print("\nError: Jugador(es) no encontrado(s).")
        return

    actualizar_estadisticas_partido(id_jugador1, resultado_jugador1)
    actualizar_estadisticas_partido(id_jugador2, resultado_jugador2)

    print("\nPartido registrado exitosamente.")

def mostrar_resultados():
    print("\nResultados del Torneo:")
    for jugador in jugadores.values():
        print(f"{jugador['Nombre']} (ID: {jugador['Id Jugador']}) - PJ: {jugador['PJ']} | PG: {jugador['PG']} | PP: {jugador['PP']} | PA: {jugador['PA']} | TP: {jugador['TP']}")

def conocer_ganador_por_categoria(categoria):
    ganador = obtener_ganador_por_categoria(categoria)

    if ganador:
        print(f"\nGanador en la categoría {categoria}: {ganador['Nombre']} (ID: {ganador['Id Jugador']})")
        print(f"Puntos a favor (PA): {ganador['PA']}")
