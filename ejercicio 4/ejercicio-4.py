
total_numeros = 0
total_pares = 0
suma_pares = 0
total_impares = 0
suma_impares = 0
menores_que_10 = 0
entre_20_y_50 = 0
mayores_que_100 = 0


while True:
    numero = int(input("Ingrese un número (ingrese un número negativo para terminar): "))

    if numero < 0:
        break  

    
    total_numeros += 1

    if numero % 2 == 0:
        total_pares += 1
        suma_pares += numero
    else:
        total_impares += 1
        suma_impares += numero

    if numero < 10:
        menores_que_10 += 1
    elif 20 <= numero <= 50:
        entre_20_y_50 += 1
    elif numero > 100:
        mayores_que_100 += 1


promedio_pares = suma_pares / total_pares if total_pares > 0 else 0
promedio_impares = suma_impares / total_impares if total_impares > 0 else 0

print("\nReporte:")
print("Total de números ingresados:", total_numeros)
print("Total de números pares ingresados:", total_pares)
print("Promedio de los números pares:", promedio_pares)
print("Promedio de los números impares:", promedio_impares)
print("Cuantos números son menores que 10:", menores_que_10)
print("Cuantos números están entre 20 y 50:", entre_20_y_50)
print("Cuantos números son mayores que 100:", mayores_que_100)