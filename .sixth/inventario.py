#código, nombre,  stock actual,  mínimo que necesitamos
inventario = [
    [101, "Teclado", 5, 10],
    [102, "Mouse", 1, 10],
    [103, "Monitor", 3, 8],
    [104, "Impresora", 7, 7],
    [105, "USB", 2, 12]
]


def calcular_pedido(stock, minimo):
    if stock < minimo:
        return minimo - stock
    else:
        return 0


print("Lista de pedidos:\n")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print(f"Artículo: {nombre}")
    print(f"Cantidad a pedir: {cantidad_pedir}")
