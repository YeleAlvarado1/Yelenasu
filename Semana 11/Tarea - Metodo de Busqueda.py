# Crear una matriz de (3x3)
matriz1 = [
    [1, 2, 4],
    [7, 8, 3],
    [5, 1, 6]
]

# Valor a buscar
valor_buscado = 6

# Ordenar las filas de la matriz por el valor máximo en cada fila
matriz1.sort(key=lambda fila: max(fila))

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor_buscado):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == valor_buscado:
                return (i, j)
    return None

# Función para imprimir la matriz con el valor buscado resaltado
def imprimir_matriz_con_resaltado(matriz, valor_buscado, posicion):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if (i, j) == posicion:
                # Resaltamos el valor buscado
                print(f"[{valor_buscado:2d}]", end=" ")
            else:
                print(f"{valor:2d}", end=" ")
        print()

# Llamar a la función de búsqueda
posicion = buscar_valor(matriz1, valor_buscado)

# Mostrar la matriz ordenada
print("Matriz Ordenada por Valor Máximo en Cada Fila:")
for fila in matriz1:
    print(fila)

# Mostrar la matriz con el valor buscado resaltado y su posición
print("\nMatriz con Valor Buscado Resaltado:")
if posicion:
    imprimir_matriz_con_resaltado(matriz1, valor_buscado, posicion)
    print(f"\nEl valor {valor_buscado} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
    # Imprimir la matriz sin resaltado si no se encuentra el valor
    for fila in matriz1:
        print(" ".join(map(str, fila)))