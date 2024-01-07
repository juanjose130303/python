from gestion import Gestion
from camper import Camper
from ruta_entrenamiento import RutaEntrenamiento
from entrenador import Entrenador
from matricula import Matricula

def menu_principal():
    print("1. Registrar nuevo Camper")
    print("2. Registrar nota de prueba")
    print("3. Gestionar matrícula")
    print("4. Consultar información")
    print("5. Guardar y salir")

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

def registrar_nota_prueba(campers):
    print("Registro de nota de prueba:")
    nro_identificacion = input("Número de identificación del Camper: ")
    camper = Gestion.buscar_camper_por_identificacion(campers, nro_identificacion)
    if camper and camper.estado == "Inscrito":
        nota_teorica = Gestion.input_float("Ingrese la nota teórica: ")
        nota_practica = Gestion.input_float("Ingrese la nota práctica: ")
        quices = Gestion.input_float("Ingrese la nota de quices: ")
        trabajos = Gestion.input_float("Ingrese la nota de trabajos: ")
        Gestion.asignar_notas(camper, nota_teorica, nota_practica, quices, trabajos)
        print("Notas registradas exitosamente.")
    else:
        print("Camper no encontrado o no está inscrito.")

def gestionar_matricula(campers, rutas, entrenadores):
    print("Gestión de matrícula:")
    nro_identificacion = input("Número de identificación del Camper: ")
    camper = Gestion.buscar_camper_por_identificacion(campers, nro_identificacion)
    if camper and camper.estado == "Aprobado":
        print("Seleccione la ruta de entrenamiento:")
        Gestion.mostrar_rutas_entrenamiento(rutas)
        id_ruta = input("ID de la ruta seleccionada: ")
        ruta = Gestion.buscar_ruta_por_id(rutas, id_ruta)
        if ruta and Gestion.verificar_capacidad_ruta(ruta, campers):
            print("Seleccione el entrenador:")
            Gestion.mostrar_entrenadores(entrenadores)
            id_entrenador = input("ID del entrenador seleccionado: ")
            entrenador = Gestion.buscar_entrenador_por_id(entrenadores, id_entrenador)
            if entrenador:
                fecha_inicio = input("Fecha de inicio de la matrícula: ")
                fecha_fin = input("Fecha de finalización de la matrícula: ")
                salon_entrenamiento = input("Salón de entrenamiento: ")
                matricula = Gestion.gestionar_matricula(camper, ruta, entrenador, fecha_inicio, fecha_fin, salon_entrenamiento)
                print("Matrícula gestionada exitosamente.")
            else:
                print("Entrenador no encontrado.")
        else:
            print("Ruta no encontrada o sin capacidad disponible.")
    else:
        print("Camper no encontrado o no aprobado.")

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

def main():
    campers, rutas, entrenadores = Gestion.cargar_datos()

    while True:
        menu_principal()
        opcion = Gestion.input_numero("Seleccione una opción: ")

        if opcion == 1:
            registrar_camper(campers)
        elif opcion == 2:
            registrar_nota_prueba(campers)
        elif opcion == 3:
            gestionar_matricula(campers, rutas, entrenadores)
        elif opcion == 4:
            consultar_informacion(campers, rutas, entrenadores)
        elif opcion == 5:
            Gestion.guardar_datos(campers, rutas, entrenadores)
            print("Datos guardados exitosamente. Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
