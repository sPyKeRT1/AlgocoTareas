import random

def generar_matriz(filas, columnas):
    return [random.sample(range(1, columnas + 1), columnas) for _ in range(filas)]

def escribir_matriz_en_linea(matriz):
    return " | ".join(" ".join(map(str, fila)) for fila in matriz)

def crear_archivo_matrices(cantidad,minimo,maximo,tipo):
    with open("pares_matrices.txt", "w") as archivo:
        if(tipo == 1):
            for i in range(cantidad):
                n = random.randint(minimo, maximo)
                matriz1 = generar_matriz(n, n)
                matriz2 = generar_matriz(n, n)
                archivo.write(escribir_matriz_en_linea(matriz1) + "\n")
                archivo.write(escribir_matriz_en_linea(matriz2) + "\n")
        elif(tipo == 2):
            for i in range(cantidad):
                filas1 = random.randint(minimo, maximo)
                columnas1 = random.randint(minimo, maximo)
                columnas2 = random.randint(minimo, maximo)
                matriz1 = generar_matriz(filas1, columnas1)
                matriz2 = generar_matriz(columnas1, columnas2)
                archivo.write(escribir_matriz_en_linea(matriz1) + "\n")
                archivo.write(escribir_matriz_en_linea(matriz2) + "\n")

A = int(input("Ingrese el número de pares matrices: "))
B = int(input("Ingrese el tamaño minimo de las matrices: "))
C = int(input("Ingrese el tamaño maximo de las matrices: "))
D = int(input("Ingrese 1 para Matrices de IGUAL dimension o 2 para DISTINTA dimension: "))
crear_archivo_matrices(A,B,C,D)