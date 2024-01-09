# En el archivo ruta_entrenamiento.py
class RutaEntrenamiento:
    from entrenador import Entrenador

    def __init__(self, id_ruta, nombre, areas_entrenamiento, capacidad_maxima, sgdb_principal, sgdb_alternativo):
        self.id_ruta = id_ruta
        self.nombre = nombre
        self.areas_entrenamiento = areas_entrenamiento
        self.capacidad_maxima = capacidad_maxima
        self.sgdb_principal = sgdb_principal
        self.sgdb_alternativo = sgdb_alternativo
        self.campers_asignados = []
        self.entrenador_asignado = None

    @staticmethod
    def crear_nueva_ruta():
        print("\nCreación de Nueva Ruta de Entrenamiento:")
        id_ruta = input("ID de la ruta: ")
        nombre = input("Nombre de la ruta: ")
        areas_entrenamiento = input("Áreas de entrenamiento separadas por comas: ").split(',')
        capacidad_maxima = 33  # Capacidad máxima de campers
        sgdb_principal = input("SGDB Principal: ")
        sgdb_alternativo = input("SGDB Alternativo: ")

        nueva_ruta = RutaEntrenamiento(id_ruta, nombre, areas_entrenamiento, capacidad_maxima, sgdb_principal, sgdb_alternativo)
        print(f"\nRuta de Entrenamiento '{nombre}' creada exitosamente.")
        return nueva_ruta
