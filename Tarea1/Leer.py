def leerlista(ruta_archivo):
    listas = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            numeros = linea.split()
            numeros = [int(num) for num in numeros]
            listas.append(numeros)
    return listas