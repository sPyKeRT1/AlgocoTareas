from Leer import leerlista #NECESARIO PARA LEER ENTRADAS
import time #NECESARIO PARA MEDIR TIEMPOS

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    mitad = len(lista) // 2
    izq = merge_sort(lista[:mitad])
    der = merge_sort(lista[mitad:])
    
    return merge(izq, der)

def merge(izq, der):
    merge = []
    i = j = 0
    
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            merge.append(izq[i])
            i += 1
        else:
            merge.append(der[j])
            j += 1
    
    merge.extend(izq[i:])
    merge.extend(der[j:])
    return merge

tiempos = []
listas = leerlista("listas_numeros.txt")
for lista in listas:
    start_time = time.time()
    merge_sort(lista)
    end_time = time.time()
    elapsed_time = end_time - start_time
    tiempos.append(elapsed_time)
print("Tiempo promedio de ejecucion: ",sum(tiempos)/len(tiempos))