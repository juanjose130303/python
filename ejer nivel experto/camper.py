class Camper:
    def __init__(self, nro_identificacion, nombre, apellidos, direccion, acudiente, nro_celular, nro_fijo, estado):
        self.nro_identificacion = nro_identificacion
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.acudiente = acudiente
        self.nro_celular = nro_celular
        self.nro_fijo = nro_fijo
        self.estado = estado
        self.notas = {
            'nota_teorica': 0,
            'nota_practica': 0,
            'quices': 0,
            'trabajos': 0
        }
    @staticmethod
    def registrar_camper():
        nro_identificacion = input("Número de identificación: ")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        direccion = input("Dirección: ")
        acudiente = input("Acudiente: ")
        nro_celular = input("Número de celular: ")
        nro_fijo = input("Número fijo: ")
        estado = "Inscrito"
        nuevo_camper = Camper(nro_identificacion, nombre, apellidos, direccion, acudiente, nro_celular, nro_fijo, estado)
        return nuevo_camper

    def actualizar_estado_aprobado(self):
        if self.estado == "Inscrito" and self.nota_teorica + self.nota_practica >= 60:
            self.estado = "Aprobado"

    @staticmethod
    def registrar_prueba(camper):
        if camper.estado == "Inscrito":
            nota_teorica = float(input("Ingrese la nota teórica: "))
            nota_practica = float(input("Ingrese la nota práctica: "))
            quices = float(input("Ingrese la nota de quices: "))
            trabajos = float(input("Ingrese la nota de trabajos: "))
            camper.nota_teorica = nota_teorica
            camper.nota_practica = nota_practica
            camper.quices = quices
            camper.trabajos = trabajos
            camper.actualizar_estado_aprobado()
            print("Notas registradas exitosamente.")
        else:
            print("No se pueden registrar notas para campers no inscritos.")