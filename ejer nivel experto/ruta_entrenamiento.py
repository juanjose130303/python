class RutaEntrenamiento:
    def __init__(self, id_ruta, nombre, areas_entrenamiento, capacidad_maxima, sgdb_principal, sgdb_alternativo):
        self.id_ruta = id_ruta
        self.nombre = nombre
        self.areas_entrenamiento = areas_entrenamiento
        self.capacidad_maxima = capacidad_maxima
        self.sgdb_principal = sgdb_principal
        self.sgdb_alternativo = sgdb_alternativo
        self.campers_asignados = []
        self.entrenador_asignado = None
