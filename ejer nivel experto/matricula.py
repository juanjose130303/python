# En el archivo matricula.py
class Matricula:
    def __init__(self, camper, ruta, entrenador, fecha_inicio, fecha_fin, salon_entrenamiento, area_entrenamiento):
        self.camper = camper
        self.ruta = ruta
        self.entrenador = entrenador
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.salon_entrenamiento = salon_entrenamiento
        self.area_entrenamiento = area_entrenamiento

    def __str__(self):
        return f"Matrícula para {self.camper.nombre} en la ruta {self.ruta.nombre}. Entrenador: {self.entrenador.nombre}. Área: {self.area_entrenamiento}."

    @staticmethod
    def gestionar_matricula(camper, ruta, entrenador, fecha_inicio, fecha_fin, salon_entrenamiento, area_entrenamiento):
        nueva_matricula = Matricula(camper, ruta, entrenador, fecha_inicio, fecha_fin, salon_entrenamiento, area_entrenamiento)
        return nueva_matricula