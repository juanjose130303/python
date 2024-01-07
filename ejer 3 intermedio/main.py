from gestion_productos import (
    registrar_producto,
    visualizar_productos,
    actualizar_stock,
    generar_informe_productos_criticos,
    calcular_ganancia_potencial_total,
    productos
)
from validaciones import (
    obtener_numero_entero,
    obtener_numero_decimal
)

def mostrar_menu():
    print("\nMenú:")
    print("1. Registrar Producto")
    print("2. Visualizar Productos")
    print("3. Actualizar Stock")
    print("4. Informe de Productos Críticos")
    print("5. Cálculo de Ganancia Potencial")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_nuevo_producto()
        elif opcion == "2":
            visualizar_productos()
        elif opcion == "3":
            actualizar_stock_producto()
        elif opcion == "4":
            generar_informe_productos_criticos()
        elif opcion == "5":
            calcular_ganancia_potencial_total()
        elif opcion == "6":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\nError: Opción no válida. Por favor, seleccione una opción correcta.")

def registrar_nuevo_producto():
    print("\nIngrese los datos del nuevo producto:")
    codigo = obtener_numero_entero("Código del producto: ")
    nombre = input("Nombre del producto: ")
    valor_compra = obtener_numero_decimal("Valor de compra del producto: ")
    valor_venta = obtener_numero_decimal("Valor de venta del producto: ")
    stock_minimo = obtener_numero_entero("Stock mínimo permitido: ")
    stock_maximo = obtener_numero_entero("Stock máximo permitido: ")
    proveedor = input("Proveedor del producto: ")

    registrar_producto(codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor)
    print(f"\nProducto '{nombre}' registrado exitosamente.")

def actualizar_stock_producto():
    if not productos:
        print("\nError: No hay productos registrados. Registre al menos un producto antes de actualizar el stock.")
        return
    
    codigo = obtener_numero_entero("\nIngrese el código del producto: ")
    cantidad = obtener_numero_entero("Ingrese la cantidad a agregar/restar al stock: ")
    actualizar_stock(codigo, cantidad)

if __name__ == "__main__":
    main()
