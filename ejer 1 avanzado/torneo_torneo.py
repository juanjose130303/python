# torneo_torneo.py

from jugadores_torneo import jugadores

def iniciar_torneo():
    # Lógica para iniciar el torneo y realizar partidos
    pass

def conocer_ganador(categoria):
    if not jugadores:
        print("\nError: No hay jugadores registrados.")
        return

    if len(jugadores) < 5:
        print("\nError: No hay suficientes jugadores para iniciar el torneo en la categoría.")
        return

    jugadores_categoria = [jugador for jugador in jugadores.values() if jugador['Categoria'] == categoria]

    if not jugadores_categoria or len(jugadores_categoria) < 5:
        print("\nError: No hay suficientes jugadores en la categoría para iniciar el torneo.")
        return

    ganador = max(jugadores_categoria, key=lambda x: x['PA'])

    print(f"\nGanador en la categoría {categoria}: {ganador['Nombre']} con {ganador['PA']} puntos a favor.")
