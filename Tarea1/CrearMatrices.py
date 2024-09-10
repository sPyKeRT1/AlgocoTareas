import random

def generar_matriz(filas, columnas):
    """Genera una matriz de tamaño filas x columnas con valores aleatorios."""
    return [[random.randint(0, 100) for _ in range(columnas)] for _ in range(filas)]

def escribir_matriz_en_linea(matriz):
    """Convierte una matriz en una cadena de texto, donde cada fila está separada por espacios."""
    return " | ".join(" ".join(map(str, fila)) for fila in matriz)

def crear_archivo_matrices():
    with open("pares_matrices.txt", "w") as archivo:
        for i in range(50):
            if i < 25:
                # Generar matrices de igual dimensión
                n = random.randint(1, 10)  # Dimensiones comunes para matrices cuadradas pequeñas
                matriz1 = generar_matriz(n, n)
                matriz2 = generar_matriz(n, n)
            else:
                # Generar matrices de distinta dimensión pero multiplicables
                filas1 = random.randint(1, 10)
                columnas1 = random.randint(1, 10)
                columnas2 = random.randint(1, 10)
                matriz1 = generar_matriz(filas1, columnas1)
                matriz2 = generar_matriz(columnas1, columnas2)

            # Escribir la primera matriz
            archivo.write(escribir_matriz_en_linea(matriz1) + "\n")
            # Escribir la segunda matriz
            archivo.write(escribir_matriz_en_linea(matriz2) + "\n")
            # Añadir una línea vacía para separar los pares
            if i < 49:  # Evitar línea vacía al final del archivo
                archivo.write("\n")

# Ejecutar el programa
crear_archivo_matrices()