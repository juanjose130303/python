nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
peso = float(input("Ingrese el peso del estudiante en Kg: "))
altura = float(input("Ingrese la altura del estudiante en metros: "))

imc = peso / (altura ** 2)


if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "Normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obeso"

print("\nInformación del estudiante:")
print("Nombre:", nombre)
print("Edad:", edad, "años")
print("IMC:", imc)
print("Categoría de IMC:", categoria)