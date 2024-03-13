import sys

def filtrar_productos(precios, umbral, condicion="mayor"):
    if condicion not in ["mayor", "menor"]:
        sys.exit("Lo sentimos, no es una operación válida.")

    productos_filtrados = {}

    for producto, precio in precios.items():
        if (condicion == "mayor" and precio > umbral) or (condicion == "menor" and precio < umbral):
            productos_filtrados[producto] = precio

    return productos_filtrados

if __name__ == "__main__":
    # Diccionario de prueba
    precios = {'Notebook': 700000,
               'Teclado': 25000,
               'Mouse': 12000,
               'Monitor': 250000,
               'Escritorio': 135000,
               'Tarjeta de Video': 1500000}

    # Obtener el umbral del primer argumento de línea de comandos
    umbral = int(sys.argv[1]) if len(sys.argv) > 1 else sys.exit("Por favor, especifique un umbral.")

    # Obtener la condición del segundo argumento de línea de comandos (por defecto es "mayor")
    condicion = sys.argv[2].lower() if len(sys.argv) > 2 else "mayor"

    # Filtrar los productos y mostrar los resultados
    productos_filtrados = filtrar_productos(precios, umbral, condicion)
    
    if productos_filtrados:
        print(f"Los productos {condicion} al umbral son: {', '.join(productos_filtrados.keys())}")
    else:
        print("No hay productos que cumplan la condición.")
