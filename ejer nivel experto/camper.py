class Camper:
    def __init__(self, nro_identificacion, nombre, apellidos, direccion, acudiente, telefono_celular, telefono_fijo, estado):
        self.nro_identificacion = nro_identificacion
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.acudiente = acudiente
        self.telefono_celular = telefono_celular
        self.telefono_fijo = telefono_fijo
        self.estado = estado
        self.rutas_asignadas = []  
        self.entrenador_asignado = None  
        self.notas = {}  
