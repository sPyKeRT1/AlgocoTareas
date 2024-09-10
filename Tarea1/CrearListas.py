import random

def generar_lista_aleatoria(n):
    return random.sample(range(1, n + 1), n)

def generar_lista_semi_ordenada(n):
    lista = sorted([random.randint(0, n) for _ in range(n)])
    num_desordenados = n // 4
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

def crear_archivo_listas(cantidad, minimo, maximo, tipo):
    with open("listas_numeros.txt", "w") as archivo: 
        if(tipo == 1):
            for i in range(cantidad):
                lista = generar_lista_aleatoria(random.randint(minimo, maximo))
                archivo.write(" ".join(map(str, lista)) + "\n")
        elif(tipo == 2):
            for i in range(cantidad):
                lista = generar_lista_semi_ordenada(random.randint(minimo, maximo))
                archivo.write(" ".join(map(str, lista)) + "\n")
        elif(tipo == 3):
            for i in range(cantidad):
                lista = generar_lista_parcialmente_ordenada(random.randint(minimo, maximo))
                archivo.write(" ".join(map(str, lista)) + "\n")

A = int(input("Ingrese el número de listas: "))
B = int(input("Ingrese el largo minimo de las listas: "))
C = int(input("Ingrese el largo maximo de las listas: "))
D = int(input("Ingrese 1 para Listas Aleatorias, 2 para Semiordenadas o 3 para Parcialmente ordenadas: "))
crear_archivo_listas(A,B,C,D)