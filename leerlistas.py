def leer_listas_desde_archivo(nombre_archivo):
    """Lee listas de números desde un archivo y devuelve una lista de listas de enteros."""
    listas = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            # Dividir la línea en números y convertirlos a enteros
            if linea.strip():  # Solo procesar si la línea no está vacía
                lista = list(map(int, linea.strip().split()))
                listas.append(lista)
    return listas

# Ejemplo de uso
listas = leer_listas_desde_archivo("listas_numeros.txt")
