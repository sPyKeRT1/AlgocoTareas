from Leer import leerlista
           
listas = leerlista("listas_numeros.txt")
for lista in listas:
    lista.sort()
    print(lista)