import json
from camper import Camper
from ruta_entrenamiento import RutaEntrenamiento
from entrenador import Entrenador
from matricula import Matricula

class Gestion:
    @staticmethod
    def cargar_datos():
        try:
            with open("campers.json", "r") as file:
                campers = json.load(file)
        except FileNotFoundError:
            campers = []

        try:
            with open("rutas.json", "r") as file:
                rutas = json.load(file)
        except FileNotFoundError:
            rutas = []

        try:
            with open("entrenadores.json", "r") as file:
                entrenadores = json.load(file)
        except FileNotFoundError:
            entrenadores = []

        try:
            with open("areas_entrenamiento.json", "r") as file:
                areas_entrenamiento = json.load(file)
        except FileNotFoundError:
            areas_entrenamiento = []

        return campers, rutas, entrenadores, areas_entrenamiento

    @staticmethod
    def guardar_datos(campers, rutas, entrenadores, areas_entrenamiento):
        with open("campers.json", "w") as file:
            json.dump(campers, file)

        with open("rutas.json", "w") as file:
            json.dump(rutas, file)

        with open("entrenadores.json", "w") as file:
            json.dump(entrenadores, file)

        with open("areas_entrenamiento.json", "w") as file:
            json.dump(areas_entrenamiento, file)

    @staticmethod
    def registrar_camper(campers):
        print("Registro de nuevo Camper:")
        nuevo_camper = Camper.registrar_camper()
        campers.append(nuevo_camper)
        print("Camper registrado exitosamente.")

    
    @staticmethod
    def inscribir_entrenador(entrenadores):
        print("Inscripción de nuevo Entrenador:")
        id_entrenador = input("ID del entrenador: ")
        nombre = input("Nombre: ")
        horario_entrenador = input("Horario del entrenador: ")  

        nuevo_entrenador = Entrenador(id_entrenador, nombre, horario_entrenador)
        entrenadores.append(nuevo_entrenador)
        print("Entrenador registrado exitosamente.")

    @staticmethod
    def asignar_ruta_a_entrenador(entrenador, rutas):
        print("Asignación de Ruta a Entrenador:")
        Gestion.mostrar_rutas_entrenamiento(rutas)
        id_ruta = input("ID de la ruta a asignar: ")
        ruta = Gestion.buscar_ruta_por_id(rutas, id_ruta)
        if ruta:
            horas_semana = Gestion.input_numero("Ingrese el límite de horas por semana: ")
            horario = input("Ingrese el horario disponible del entrenador: ")
            entrenador.asignar_ruta(ruta, horas_semana, horario)
            print(f"Ruta {ruta.nombre} asignada al entrenador {entrenador.nombre} exitosamente.")
        else:
            print("Ruta no encontrada.")

    @staticmethod
    def buscar_camper_por_identificacion(campers, nro_identificacion):
        for camper in campers:
            if camper.nro_identificacion == nro_identificacion:
                return camper
        return None

    @staticmethod
    def buscar_ruta_por_id(rutas, id_ruta):
        for ruta in rutas:
            if ruta.id_ruta == id_ruta:
                return ruta
        return None

    @staticmethod
    def mostrar_rutas_entrenamiento(rutas):
        for ruta in rutas:
            print(f"ID: {ruta.id_ruta} - Nombre: {ruta.nombre}")

    @staticmethod
    def mostrar_entrenadores(entrenadores):
        for entrenador in entrenadores:
            print(f"ID: {entrenador.id_entrenador} - Nombre: {entrenador.nombre}")

    @staticmethod
    def input_numero(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

    @staticmethod
    def input_float(mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Por favor, ingrese un número decimal válido.")
                
    @staticmethod
    def asignar_notas(camper, nota_teorica, nota_practica, quices, trabajos):
        camper.nota_teorica = nota_teorica
        camper.nota_practica = nota_practica
        camper.quices = quices
        camper.trabajos = trabajos
        
    @staticmethod
    def registrar_prueba(campers):
        print("Registro de prueba:")
        nro_identificacion = input("Número de identificación del Camper: ")
        camper = Gestion.buscar_camper_por_identificacion(campers, nro_identificacion)
        if camper:
            Camper.registrar_prueba(camper)
        else:
            print("Camper no encontrado.")

    @staticmethod
    def campers_en_riesgo(campers):
        return [camper for camper in campers if camper.estado == "Aprobado" and Gestion.calcular_promedio(camper) < 60]

    @staticmethod
    def generar_reportes(campers, rutas, entrenadores):
        print("Generación de reportes:")
        
        print("a. Listar los campers que se encuentren en estado de inscrito.")
        Gestion.mostrar_campers(Gestion.consultar_campers_en_estado(campers, "Inscrito"))

        print("b. Listar los campers que aprobaron el examen inicial.")
        campers_aprobados = Gestion.consultar_campers_aprobados(campers)
        Gestion.mostrar_campers(campers_aprobados)

        print("c. Listar los entrenadores que se encuentran trabajando con campuslands.")
        entrenadores_activos = Gestion.consultar_entrenadores_activos(entrenadores)
        Gestion.mostrar_entrenadores(entrenadores_activos)

        print("d. Listar los estudiantes que cuentan con bajo rendimiento.")
        campers_en_riesgo = Gestion.campers_en_riesgo(campers)
        Gestion.mostrar_campers(campers_en_riesgo)

        print("e. Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento.")
        print("Seleccione la ruta:")
        Gestion.mostrar_rutas_entrenamiento(rutas)
        id_ruta = input("ID de la ruta seleccionada: ")
        ruta = Gestion.buscar_ruta_por_id(rutas, id_ruta)
        if ruta:
            campers_asignados, entrenador_asociado = Gestion.consultar_campers_y_entrenador_por_ruta(ruta, campers, entrenadores)
            Gestion.mostrar_campers(campers_asignados)
            Gestion.mostrar_entrenador(entrenador_asociado)
        else:
            print("Ruta no encontrada.")

        print("f. Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.")
        resultados_aprobacion = Gestion.consultar_aprobacion_modulos(rutas, entrenadores, campers)
        Gestion.mostrar_resultados_aprobacion(resultados_aprobacion)

    
    @staticmethod
    def calcular_promedio(camper):
        return (camper.nota_teorica + camper.nota_practica + camper.quices + camper.trabajos) / 4

    @staticmethod
    def asignar_camper_a_ruta(camper, ruta, areas_entrenamiento):
        for area in areas_entrenamiento:
            if area in ruta.areas_entrenamiento and not ruta.existe_camper_en_area(camper, area):
                ruta.campers_asignados.append(camper)
                return True
        return False

    @staticmethod
    def verificar_capacidad_ruta(ruta, campers):
        return len(ruta.campers_asignados) < ruta.capacidad_maxima

    @staticmethod
    def gestionar_matricula(camper, ruta, entrenador, fecha_inicio, fecha_fin, salon_entrenamiento, area_entrenamiento):
        nueva_matricula = Matricula(camper, ruta, entrenador, fecha_inicio, fecha_fin, salon_entrenamiento, area_entrenamiento)
        ruta.campers_asignados.append(camper)
        ruta.entrenador_asignado = entrenador
        camper.estado = "Matriculado"
        return nueva_matricula


    @staticmethod
    def consultar_campers_en_estado(campers, estado):
        return [camper for camper in campers if camper.estado == estado]

    @staticmethod
    def consultar_entrenadores_activos(entrenadores):
        return [entrenador for entrenador in entrenadores if entrenador.estado == "Activo"]

    @staticmethod
    def mostrar_campers(campers):
        for camper in campers:
            print(f"ID: {camper.nro_identificacion} - Nombre: {camper.nombre} {camper.apellidos}")

    @staticmethod
    def mostrar_entrenador(entrenador):
        print(f"ID: {entrenador.id_entrenador} - Nombre: {entrenador.nombre}")

    @staticmethod
    def mostrar_resultados_aprobacion(resultados):
        for resultado in resultados:
            print(f"Ruta: {resultado['ruta']}, Entrenador: {resultado['entrenador']}, Porcentaje Aprobación: {resultado['porcentaje_aprobacion']}%")

    @staticmethod
    def consultar_campers_y_entrenador_por_ruta(ruta, campers, entrenadores):
        campers_asignados = [camper for camper in campers if camper in ruta.campers_asignados]
        entrenador_asociado = ruta.entrenador_asignado
        return campers_asignados, entrenador_asociado

    @staticmethod
    def consultar_campers_aprobados(campers):
        return [camper for camper in campers if camper.estado == "Aprobado"]

    @staticmethod
    def consultar_campers_en_riesgo(campers):
        return [camper for camper in campers if camper.estado == "Inscrito" and Gestion.calcular_promedio(camper) < 60]

    @staticmethod
    def consultar_aprobacion_modulos(rutas, entrenadores, campers):
        resultados = []
        for ruta in rutas:
            for entrenador in entrenadores:
                campers_asignados, _ = Gestion.consultar_campers_y_entrenador_por_ruta(ruta, campers, entrenadores)
                if campers_asignados and len(campers_asignados) > 0:
                    porcentaje_aprobacion = (sum([Gestion.calcular_promedio(camper) >= 60 for camper in campers_asignados]) / len(campers_asignados)) * 100
                    resultados.append({"ruta": ruta.nombre, "entrenador": entrenador.nombre, "porcentaje_aprobacion": round(porcentaje_aprobacion, 2)})
        return resultados
    
    @staticmethod
    def menu_principal():
        print("1. Registrar nuevo Camper")
        print("2. Registrar nota de prueba")
        print("3. Gestionar matrícula")
        print("4. Consultar información")
        print("5. Inscribir nuevo Entrenador")
        print("6. Asignar ruta a último Entrenador")
        print("7. Guardar y salir")
        
    @staticmethod
    def registrar_camper(campers):
        print("Registro de nuevo Camper:")
        nro_identificacion = input("Número de identificación: ")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        direccion = input("Dirección: ")
        acudiente = input("Acudiente: ")
        nro_celular = input("Número de celular: ")
        nro_fijo = input("Número fijo: ")
        estado = "Inscrito"
        nuevo_camper = Camper(nro_identificacion, nombre, apellidos, direccion, acudiente, nro_celular, nro_fijo, estado)
        campers.append(nuevo_camper)
        print("Camper registrado exitosamente.")
        
    @staticmethod
    def registrar_nota_prueba(campers, rutas, areas_entrenamiento):
        print("Registro de nota de prueba:")
        nro_identificacion = input("Número de identificación del Camper: ")
        camper = Gestion.buscar_camper_por_identificacion(campers, nro_identificacion)
        if camper and camper.estado == "Inscrito":
            nota_teorica = Gestion.input_float("Ingrese la nota teórica: ")
            nota_practica = Gestion.input_float("Ingrese la nota práctica: ")
            quices = Gestion.input_float("Ingrese la nota de quices: ")
            trabajos = Gestion.input_float("Ingrese la nota de trabajos: ")
            Gestion.asignar_notas(camper, nota_teorica, nota_practica, quices, trabajos)

            # Asigna el camper a una ruta
            for ruta in rutas:
                if Gestion.asignar_camper_a_ruta(camper, ruta, areas_entrenamiento):
                    print(f"Camper asignado a la ruta {ruta.nombre} exitosamente.")
                    break
            else:
                print("No se pudo asignar el Camper a ninguna ruta disponible.")

            print("Notas registradas exitosamente.")
        else:
            print("Camper no encontrado o no está inscrito.")
            
    @staticmethod
    def gestionar_matricula(camper, ruta, entrenador, fecha_inicio, fecha_fin, salon_entrenamiento, area_entrenamiento):
        nueva_matricula = Matricula(camper, ruta, entrenador, fecha_inicio, fecha_fin, salon_entrenamiento, area_entrenamiento)
        ruta.campers_asignados.append(camper)
        ruta.entrenador_asignado = entrenador
        camper.estado = "Matriculado"
        return nueva_matricula
    
    @staticmethod
    def main():
        campers, rutas, entrenadores, areas_entrenamiento = Gestion.cargar_datos()

        while True:
            Gestion.menu_principal()
            opcion = Gestion.input_numero("Seleccione una opción: ")

            if opcion == 1:
                Gestion.registrar_camper(campers)
            elif opcion == 2:
                Gestion.registrar_nota_prueba(campers, rutas, areas_entrenamiento)
            elif opcion == 3:
                Gestion.gestionar_matricula(campers, rutas, entrenadores)
            elif opcion == 4:
                Gestion.consultar_informacion(campers, rutas, entrenadores)
            elif opcion == 5:
                Gestion.inscribir_entrenador(entrenadores)
            elif opcion == 6:
                Gestion.asignar_ruta_a_entrenador(entrenadores[-1], rutas)
            elif opcion == 7:
                Gestion.guardar_datos(campers, rutas, entrenadores, areas_entrenamiento)
                print("Datos guardados exitosamente. Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    @staticmethod
    def consultar_informacion(campers, rutas, entrenadores):
        print("Consulta de información:")
        print("1. Campers en estado de inscrito")
        print("2. Campers que aprobaron el examen inicial")
        print("3. Entrenadores activos")
        print("4. Campers con bajo rendimiento")
        print("5. Campers y entrenador por ruta")
        print("6. Aprobación de módulos por ruta y entrenador")

        opcion = Gestion.input_numero("Seleccione una opción: ")

        if opcion == 1:
            campers_inscritos = Gestion.consultar_campers_en_estado(campers, "Inscrito")
            Gestion.mostrar_campers(campers_inscritos)
        elif opcion == 2:
            campers_aprobados = Gestion.consultar_campers_aprobados(campers)
            Gestion.mostrar_campers(campers_aprobados)
        elif opcion == 3:
            entrenadores_activos = Gestion.consultar_entrenadores_activos(entrenadores)
            Gestion.mostrar_entrenadores(entrenadores_activos)
        elif opcion == 4:
            campers_en_riesgo = Gestion.consultar_campers_en_riesgo(campers)
            Gestion.mostrar_campers(campers_en_riesgo)
        elif opcion == 5:
            print("Seleccione la ruta:")
            Gestion.mostrar_rutas_entrenamiento(rutas)
            id_ruta = input("ID de la ruta seleccionada: ")
            ruta = Gestion.buscar_ruta_por_id(rutas, id_ruta)
            if ruta:
                campers_asignados, entrenador_asociado = Gestion.consultar_campers_y_entrenador_por_ruta(ruta, campers, entrenadores)
                Gestion.mostrar_campers(campers_asignados)
                Gestion.mostrar_entrenador(entrenador_asociado)
            else:
                print("Ruta no encontrada.")
        elif opcion == 6:
            resultados_aprobacion = Gestion.consultar_aprobacion_modulos(rutas, entrenadores, campers)
            Gestion.mostrar_resultados_aprobacion(resultados_aprobacion)
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    Gestion.menu_principal()
