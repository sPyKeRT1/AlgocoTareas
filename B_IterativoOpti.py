def transponer_matriz(M):
    filas = len(M)
    columnas = len(M[0])
    return [[M[j][i] for j in range(filas)] for i in range(columnas)]

def multiplicacion_matrices_optimizada(A, B):
    # Transponemos la matriz B para mejorar la localidad de los datos
    B_t = transponer_matriz(B)

    # Dimensiones de las matrices
    filas_A = len(A)
    columnas_A = len(A[0])
    filas_B = len(B)
    columnas_B = len(B[0])

    # Asegurarse de que el número de columnas de A es igual al número de filas de B
    if columnas_A != filas_B:
        raise ValueError("Las matrices no se pueden multiplicar")

    # Crear la matriz resultante C con ceros, de dimensiones filas_A x columnas_B
    C = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

    # Iteración cúbica para multiplicar matrices
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                C[i][j] += A[i][k] * B_t[j][k]

    return C

# Ejemplo de uso
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

resultado = multiplicacion_matrices_optimizada(A, B)
for fila in resultado:
    print(fila)