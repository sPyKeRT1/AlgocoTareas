from Leer import leerlista #NECESARIO PARA LEER ENTRADAS
import time #NECESARIO PARA MEDIR TIEMPOS
           
tiempos = []
listas = leerlista("listas_numeros.txt")
for lista in listas:
    start_time = time.time()
    lista.sort()
    end_time = time.time()
    elapsed_time = end_time - start_time
    tiempos.append(elapsed_time)
print("Tiempo promedio de ejecucion: ",sum(tiempos)/len(tiempos))