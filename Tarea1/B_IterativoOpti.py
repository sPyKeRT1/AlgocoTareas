from Leer import leermatrices

def transponer_matriz(Matriz):
    filas = len(Matriz)
    columnas = len(Matriz[0])
    return [[Matriz[j][i] for j in range(filas)] for i in range(columnas)]

def multiplicacion_matrices_optimizada(A, B):
    B_t = transponer_matriz(B)

    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])

    C = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                C[i][j] += A[i][k] * B_t[j][k]

    return C

pares_matrices = leermatrices("pares_matrices.txt")
for (A, B) in pares_matrices:
    print( multiplicacion_matrices_optimizada(A, B))