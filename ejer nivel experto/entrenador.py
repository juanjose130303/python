class Entrenador:
    def __init__(self, id_entrenador, nombre, horario_entrenador):
        self.id_entrenador = id_entrenador
        self.nombre = nombre
        self.horario_entrenador = horario_entrenador
        self.rutas_asignadas = []

    def asignar_ruta(self, ruta):
        if self.horario_entrenador.lower() == 'activo' and ruta not in self.rutas_asignadas:
            self.rutas_asignadas.append(ruta)
            return True
        return False

    def __str__(self):
        return f"ID: {self.id_entrenador}, Nombre: {self.nombre}, Horario: {self.horario_entrenador}, Rutas Asignadas: {self.rutas_asignadas}"
