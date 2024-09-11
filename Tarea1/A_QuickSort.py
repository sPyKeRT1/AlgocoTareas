from Leer import leerlista #NECESARIO PARA LEER ENTRADAS
import time #NECESARIO PARA MEDIR TIEMPOS

def particion(lista, menor, mayor):
    pivote = lista[mayor]
    i = menor - 1

    for j in range(menor, mayor):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i+1], lista[mayor] = lista[mayor], lista[i+1]
    return i+1

def quick_sort(lista, menor = 0, mayor = None):
    if mayor is None:
        mayor = len(lista) - 1

    if menor < mayor:
        indice_pivote = particion(lista, menor, mayor)
        quick_sort(lista, menor, indice_pivote - 1)
        quick_sort(lista, indice_pivote + 1, mayor)

tiempos = []
listas = leerlista("listas_numeros.txt")
for lista in listas:
    start_time = time.time()
    quick_sort(lista)
    end_time = time.time()
    elapsed_time = end_time - start_time
    tiempos.append(elapsed_time)
print("Tiempo promedio de ejecucion: ",sum(tiempos)/len(tiempos))