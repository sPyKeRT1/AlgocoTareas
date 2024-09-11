from Leer import leerlista #NECESARIO PARA LEER ENTRADAS
import time #NECESARIO PARA MEDIR TIEMPOS

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        if not intercambiado: break
    return lista         

tiempos = []
listas = leerlista("listas_numeros.txt")
for lista in listas:
    start_time = time.time()
    bubble_sort(lista)
    end_time = time.time()
    elapsed_time = end_time - start_time
    tiempos.append(elapsed_time)
print("Tiempo promedio de ejecucion: ",sum(tiempos)/len(tiempos))