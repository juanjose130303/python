def registrar_ciudad(ciudades):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    ciudades.append({'ciudad': ciudad, 'sismos': []})
    print(f"Ciudad {ciudad} registrada con éxito.")

def registrar_sismo(ciudades):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    magnitud = float(input("Ingrese la magnitud del sismo: "))
    ciudades_encontradas = [c for c in ciudades if c['ciudad'] == ciudad]

    if ciudades_encontradas:
        ciudades_encontradas[0]['sismos'].append(magnitud)
        print("Sismo registrado con éxito.")
    else:
        print("Ciudad no encontrada.")

def buscar_sismos(ciudades):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    ciudades_encontradas = [c for c in ciudades if c['ciudad'] == ciudad]

    if ciudades_encontradas:
        sismos = ciudades_encontradas[0]['sismos']
        print(f"Sismos registrados en {ciudad}: {sismos}")
    else:
        print("Ciudad no encontrada.")

def informe_riesgo(ciudades):
    for ciudad_info in ciudades:
        ciudad = ciudad_info['ciudad']
        sismos = ciudad_info['sismos']

        if sismos:
            promedio = sum(sismos) / len(sismos)

            if promedio < 2.5:
                print(f"Riesgo en {ciudad}: Amarillo (Sin riesgo)")
            elif 2.6 <= promedio <= 4.5:
                print(f"Riesgo en {ciudad}: Naranja (Riesgo medio)")
            else:
                print(f"Riesgo en {ciudad}: Rojo (Riesgo alto)")
        else:
            print(f"No hay sismos registrados en {ciudad}.")

