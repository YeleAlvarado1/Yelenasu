# Definimos una matriz 3x3
matriz2 = [
    [3, 1, 2],
    [7, 8, 5],
    [9, 4, 6]
]
# Función para ordenar una lista  en la matriz
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    left = [x for x in lista if x < pivot]
    middle = [x for x in lista if x == pivot]
    right = [x for x in lista if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Ordenar Matriz
def ordenar_matriz_como_lista(matriz2):

# Convertir la matriz en una lista unidimensional
    lista = [elemento for fila in matriz2 for elemento in fila]

# Ordenar la lista
    lista_ordenada = quicksort(lista)

# Reconstruir la matriz ordenada
    filas = len(matriz2)
    columnas = len(matriz2[0])
    matriz2_ordenada = []
    for i in range(filas):
        fila = lista_ordenada[i * columnas:(i + 1) * columnas]
        matriz2_ordenada.append(fila)

    return matriz2_ordenada

def imprimir_matriz(matriz2):
#Imprime la matriz de manera formateada.

    for fila in matriz2:
        print(fila)

# Imprimimos la matriz original
print("Matriz Original:")
imprimir_matriz(matriz2)

# Ordenamos la matriz como una lista unidimensional
matriz2_ordenada = ordenar_matriz_como_lista(matriz2)

# Imprimimos la matriz con los elementos ordenados
print("\nMatriz con Elementos Ordenados:")
imprimir_matriz(matriz2_ordenada)