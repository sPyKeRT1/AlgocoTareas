import random

def generar_lista_aleatoria(n):
    return random.sample(range(1, n + 1), n)

def generar_lista_semi_ordenada(n):
    lista = sorted([random.randint(0, n) for _ in range(n)])
    num_desordenados = n // 2
    for _ in range(num_desordenados):
        idx1 = random.randint(0, n - 1)
        idx2 = random.randint(0, n - 1)
        lista[idx1], lista[idx2] = lista[idx2], lista[idx1]
    return lista

def generar_lista_parcialmente_ordenada(n):
    punto_corte = n // 2
    lista_ordenada = sorted([random.randint(0, n) for _ in range(punto_corte)])
    lista_desordenada = [random.randint(0, n) for _ in range(n - punto_corte)]
    return lista_ordenada + lista_desordenada

def crear_archivo_listas(cantidad, minimo, maximo):
    with open("listas_numeros.txt", "w") as archivo:
        for i in range(cantidad):
            n = random.randint(minimo, maximo)
            if i < (cantidad // 3):
                lista = generar_lista_aleatoria(n)
            elif i < ((cantidad * 2) // 3):
                lista = generar_lista_semi_ordenada(n)
            else:
                lista = generar_lista_parcialmente_ordenada(n)
            
            archivo.write(" ".join(map(str, lista)) + "\n")

crear_archivo_listas(15,10,30)