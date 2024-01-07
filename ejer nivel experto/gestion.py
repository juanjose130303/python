import json
from camper import Camper
from ruta_entrenamiento import RutaEntrenamiento
from entrenador import Entrenador
from matricula import Matricula

class Gestion:
    @staticmethod
    def cargar_datos():
        try:
            with open('datos.json', 'r') as file:
                data = json.load(file)
                campers = [Camper(**camper_data) for camper_data in data.get('campers', [])]
                rutas = [RutaEntrenamiento(**ruta_data) for ruta_data in data.get('rutas', [])]
                entrenadores = [Entrenador(**entrenador_data) for entrenador_data in data.get('entrenadores', [])]
                return campers, rutas, entrenadores
        except FileNotFoundError:
            return [], [], []

    @staticmethod
    def guardar_datos(campers, rutas, entrenadores):
        data = {
            'campers': [camper.__dict__ for camper in campers],
            'rutas': [ruta.__dict__ for ruta in rutas],
            'entrenadores': [entrenador.__dict__ for entrenador in entrenadores],
        }
        with open('datos.json', 'w') as file:
            json.dump(data, file, indent=2)
    
    @staticmethod
    def mostrar_entrenadores(entrenadores):
        print("\nListado de Entrenadores:")
        if not entrenadores:
            print("No hay entrenadores registrados.")
        else:
            for entrenador in entrenadores:
                print(f"ID: {entrenador.id_entrenador}, Nombre: {entrenador.nombre}, Horario: {entrenador.horario_entrenador}")
    
    @staticmethod        
    def mostrar_campers(campers):
        print("\nListado de Campers:")
        if not campers:
            print("No hay campers registrados.")
        else:
            for camper in campers:
                print(f"ID: {camper.nro_identificacion}, Nombre: {camper.nombre} {camper.apellidos}, Estado: {camper.estado}")

    @staticmethod
    def mostrar_rutas_entrenamiento(rutas):
        print("\nListado de Rutas de Entrenamiento:")
        if not rutas:
            print("No hay rutas de entrenamiento registradas.")
        else:
            for ruta in rutas:
                print(f"ID: {ruta.id_ruta}, Nombre: {ruta.nombre}, SGDB Principal: {ruta.sgdb_principal}, SGDB Alternativo: {ruta.sgdb_alternativo}")
    
    @staticmethod
    def mostrar_resultados_aprobacion(resultados_aprobacion):
        print("\nResultados de Aprobación por Ruta y Entrenador:")
        if not resultados_aprobacion:
            print("No hay resultados de aprobación registrados.")
        else:
            for key, value in resultados_aprobacion.items():
                ruta_nombre, entrenador_id = key
                print(f"Ruta: {ruta_nombre}, Entrenador ID: {entrenador_id}, Aprobados: {value['aprobados']}, Perdidos: {value['perdidos']}")
                            
    @staticmethod
    def input_numero(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido.")

    @staticmethod
    def input_float(mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Error: Por favor, ingrese un número decimal válido.")

    @staticmethod
    def buscar_camper_por_identificacion(campers, nro_identificacion):
        for camper in campers:
            if camper.nro_identificacion == nro_identificacion:
                return camper
        return None

    @staticmethod
    def gestionar_matricula(camper, ruta, entrenador, fecha_inicio, fecha_fin, salon_entrenamiento):
        matricula = Matricula(camper, ruta, entrenador, fecha_inicio, fecha_fin, salon_entrenamiento)
        return matricula

    @staticmethod
    def asignar_notas(camper, nota_teorica, nota_practica, quices, trabajos):
        camper.notas = {
            'nota_teorica': nota_teorica,
            'nota_practica': nota_practica,
            'quices': quices,
            'trabajos': trabajos
        }

    @staticmethod
    def consultar_campers_en_estado(campers, estado):
        return [camper for camper in campers if camper.estado == estado]

    @staticmethod
    def consultar_campers_aprobados(campers):
        return [camper for camper in campers if Gestion.calcular_promedio(camper) >= 60]

    @staticmethod
    def consultar_entrenadores_activos(entrenadores):
        return [entrenador for entrenador in entrenadores if entrenador.horario_entrenador.lower() == 'activo']

    @staticmethod
    def consultar_campers_en_riesgo(campers):
        return [camper for camper in campers if Gestion.calcular_promedio(camper) < 60]

    @staticmethod
    def consultar_campers_y_entrenador_por_ruta(ruta, campers, entrenadores):
        campers_asignados = [camper for camper in campers if ruta.id_ruta in camper.rutas_asignadas]
        entrenador_asociado = Gestion.obtener_entrenador_por_ruta(ruta, entrenadores)
        return campers_asignados, entrenador_asociado

    @staticmethod
    def consultar_aprobacion_modulos(rutas, entrenadores, campers):
        resultados = {}
        for ruta in rutas:
            for entrenador_id in ruta.entrenadores_asignados:
                key = (ruta.nombre, entrenador_id)
                if key not in resultados:
                    resultados[key] = {'aprobados': 0, 'perdidos': 0}

                aprobados, perdidos = Gestion.contar_aprobaciones_modulo(ruta, entrenador_id, campers)
                resultados[key]['aprobados'] += aprobados
                resultados[key]['perdidos'] += perdidos

        return resultados

    @staticmethod
    def contar_aprobaciones_modulo(ruta, entrenador_id, campers):
        aprobados = 0
        perdidos = 0

        for camper in campers:
            if ruta.id_ruta in camper.rutas_asignadas and camper.entrenador_asignado == entrenador_id:
                promedio = Gestion.calcular_promedio(camper)
                if promedio >= 60:
                    aprobados += 1
                else:
                    perdidos += 1

        return aprobados, perdidos

    @staticmethod
    def calcular_promedio(camper):
        return (camper.notas['nota_teorica'] * 0.3) + (camper.notas['nota_practica'] * 0.6) + (camper.notas['quices'] * 0.1) + (camper.notas['trabajos'] * 0.1)

    @staticmethod
    def obtener_entrenador_por_ruta(ruta, entrenadores):
        for entrenador in entrenadores:
            if ruta.id_ruta in entrenador.rutas_asignadas:
                return entrenador
        return None
