# gestion_productos.py

productos = []

def registrar_producto(codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor):
    producto = {
        'codigo': codigo,
        'nombre': nombre,
        'valor_compra': valor_compra,
        'valor_venta': valor_venta,
        'stock_actual': 0,
        'stock_minimo': stock_minimo,
        'stock_maximo': stock_maximo,
        'proveedor': proveedor
    }
    productos.append(producto)

def visualizar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        print("\nLista de Productos:")
        for producto in productos:
            print(f"\nCódigo: {producto['codigo']}\nNombre: {producto['nombre']}\n"
                  f"Valor Compra: {producto['valor_compra']}\nValor Venta: {producto['valor_venta']}\n"
                  f"Stock Actual: {producto['stock_actual']}\nStock Mínimo: {producto['stock_minimo']}\n"
                  f"Stock Máximo: {producto['stock_maximo']}\nProveedor: {producto['proveedor']}")

def actualizar_stock(codigo, cantidad):
    producto = obtener_producto_por_codigo(codigo)
    if producto:
        producto['stock_actual'] += cantidad
        print(f"\nStock actualizado. Nuevo stock de {producto['nombre']}: {producto['stock_actual']}")
    else:
        print(f"\nError: Producto con código {codigo} no encontrado. No se pudo actualizar el stock.")

def obtener_producto_por_codigo(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            return producto
    return None

def generar_informe_productos_criticos():
    productos_criticos = [producto for producto in productos if producto['stock_actual'] < producto['stock_minimo']]
    
    if productos_criticos:
        print("\nProductos Críticos:")
        for producto in productos_criticos:
            print(f"\nCódigo: {producto['codigo']}\nNombre: {producto['nombre']}\n"
                  f"Stock Actual: {producto['stock_actual']}\nStock Mínimo: {producto['stock_minimo']}")
    else:
        print("\nNo hay productos críticos en stock.")

def calcular_ganancia_potencial_total():
    ganancia_total = sum((producto['valor_venta'] - producto['valor_compra']) * producto['stock_actual'] for producto in productos)
    print(f"\nGanancia Potencial Total: {ganancia_total}")
