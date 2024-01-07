jugadores = {}

def validar_edad(categoria, edad):
    if categoria == 'Novato' and not (15 <= edad <= 16):
        return False
    elif categoria == 'Intermedio' and not (17 <= edad <= 20):
        return False
    elif categoria == 'Avanzado' and edad <= 20:
        return False
    return True

def validar_existencia_jugador(id_jugador):
    return id_jugador in jugadores

def registrar_jugador(id_jugador, nombre, categoria, edad):
    if not validar_edad(categoria, edad):
        print("\nError: Edad no válida para la categoría.")
        return

    if validar_existencia_jugador(id_jugador):
        print("\nError: Jugador con ID ya registrado.")
        return

    jugador = {'Id Jugador': id_jugador, 'Nombre': nombre, 'Edad': edad, 'Categoria': categoria,
               'PJ': 0, 'PG': 0, 'PP': 0, 'PA': 0, 'TP': 0}
    jugadores[id_jugador] = jugador

def mostrar_registro():
    print("\nRegistro de Jugadores:")
    print("{:<15} {:<15} {:<10} {:<5} {:<5} {:<5} {:<5} {:<5}".format('Nombre', 'Id Jugador', 'Categoria',
                                                                        'Edad', 'PJ', 'PG', 'PP', 'PA', 'TP'))
    for jugador in jugadores.values():
        print("{:<15} {:<15} {:<10} {:<5} {:<5} {:<5} {:<5} {:<5}".format(jugador['Nombre'], jugador['Id Jugador'],
                                                                            jugador['Categoria'], jugador['Edad'],
                                                                            jugador['PJ'], jugador['PG'],
                                                                            jugador['PP'], jugador['PA'], jugador['TP']))

def actualizar_estadisticas_partido(id_jugador, resultado):
    jugador = jugadores.get(id_jugador)
    if jugador:
        jugador['PJ'] += 1
        if resultado == 'Ganado':
            jugador['PG'] += 1
            jugador['PA'] += 1  # Ajuste aquí
        elif resultado == 'Perdido':
            jugador['PP'] += 1
        jugador['TP'] += 2 * jugador['PG']
    else:
        print("\nError: Jugador no encontrado.")

def obtener_jugadores_por_categoria(categoria):
    return [jugador for jugador in jugadores.values() if jugador['Categoria'] == categoria]

def obtener_ganador_por_categoria(categoria):
    jugadores_categoria = obtener_jugadores_por_categoria(categoria)

    if len(jugadores_categoria) < 5:
        print(f"\nError: No hay suficientes jugadores en la categoría {categoria}. Se requieren al menos 5.")
        return None

    ganador = max(jugadores_categoria, key=lambda jugador: jugador['PA'])
    return ganador

