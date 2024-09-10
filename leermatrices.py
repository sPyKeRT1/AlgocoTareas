def leer_matrices_desde_archivo(nombre_archivo):
    """Lee pares de matrices desde un archivo y devuelve una lista de tuplas de matrices."""
    pares_matrices = []
    with open(nombre_archivo, "r") as archivo:
        matriz1, matriz2 = [], []
        leyendo_matriz1 = True
        
        for linea in archivo:
            if linea.strip() == "":
                # Línea vacía significa que hemos terminado de leer un par de matrices
                if matriz1 and matriz2:
                    pares_matrices.append((matriz1, matriz2))
                    matriz1, matriz2 = [], []  # Reiniciar para el siguiente par
                leyendo_matriz1 = True
            else:
                # Leer la matriz correspondiente
                matriz_fila = [list(map(int, fila.split())) for fila in linea.split(" | ")]
                if leyendo_matriz1:
                    matriz1 = matriz_fila
                    leyendo_matriz1 = False
                else:
                    matriz2 = matriz_fila

        # Añadir el último par de matrices si no se ha añadido ya
        if matriz1 and matriz2:
            pares_matrices.append((matriz1, matriz2))
    
    return pares_matrices

# Ejemplo de uso
pares = leer_matrices_desde_archivo("pares_matrices.txt")
