peso_ideal = 0
obesidad_grado_i = 0
obesidad_grado_ii = 0
obesidad_grado_iii = 0
sobrepeso = 0


for _ in range(20):
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        peso = float(input("Ingrese el peso del estudiante en Kg: "))
        altura = float(input("Ingrese la altura del estudiante en metros: "))

imc = peso / (altura ** 2)

    
if 18.5 <= imc < 24.9:
        peso_ideal += 1
elif 25 <= imc < 29.9:
        sobrepeso += 1
elif 30 <= imc < 34.9:
        obesidad_grado_i += 1
elif 35 <= imc < 39.9:
        obesidad_grado_ii += 1
elif imc >= 40:
        obesidad_grado_iii += 1

print("\nReporte de Salud de la Comunidad Estudiantil:")
print("Estudiantes en peso ideal:", peso_ideal)
print("Estudiantes en obesidad grado I:", obesidad_grado_i)
print("Estudiantes en obesidad grado II:", obesidad_grado_ii)
print("Estudiantes en obesidad grado III:", obesidad_grado_iii)
print("Estudiantes en sobrepeso:", sobrepeso)