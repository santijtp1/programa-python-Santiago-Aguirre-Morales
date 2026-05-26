# Lista para guardar los artículos
inventario = []

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Pedir cantidad de artículos
cantidad_articulos = int(input("¿Cuántos artículos desea registrar?: "))

# Ciclo para ingresar datos
for i in range(cantidad_articulos):
    print("\nArtículo", i + 1)

    # Códigos automáticos: ART1, ART2, ART3...
    codigo = "ART" + str(i + 1)

    nombre = input("Ingrese el nombre del artículo: ")
    stock_actual = int(input("Ingrese el stock actual: "))
    stock_minimo = int(input("Ingrese el stock mínimo requerido: "))

    # Guardar datos en la matriz
    inventario.append([codigo, nombre, stock_actual, stock_minimo])

# Mostrar resultados
print("\nLISTA DE REABASTECIMIENTO")
print("--------------------------------")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("\nCódigo:", codigo)
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)