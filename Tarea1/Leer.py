def leerlista(archivo):
    listas = []
    with open(archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            numeros = linea.split()
            numeros = [int(num) for num in numeros]
            listas.append(numeros)
    return listas

def leermatrices(nombre_archivo):
    pares_matrices = []
    
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.read().strip().split('\n')
        
        for i in range(0, len(lineas), 2):
            if i + 1 < len(lineas):
                matriz_a_str = lineas[i].strip()
                matrices_a = matriz_a_str.split(' | ')
                matriz_a = [list(map(int, fila.split())) for fila in matrices_a]
                
                matriz_b_str = lineas[i + 1].strip()
                matrices_b = matriz_b_str.split(' | ')
                matriz_b = [list(map(int, fila.split())) for fila in matrices_b]
                
                pares_matrices.append((matriz_a, matriz_b))
    
    return pares_matrices