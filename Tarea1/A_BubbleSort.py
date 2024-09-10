from Leer import leerlista

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
           
listas = leerlista("listas_numeros.txt")
for lista in listas:
    print(bubble_sort(lista))
