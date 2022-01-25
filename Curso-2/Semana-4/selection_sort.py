

def ordena(lista):

    total = len(lista)
    for i in range(total-1):    
        menor = i
        for j in range(i+1, total):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    
    return lista

