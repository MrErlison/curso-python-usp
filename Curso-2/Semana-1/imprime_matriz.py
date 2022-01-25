
def imprime_matriz(matriz):

    linhas = len(matriz)

    for i in range(linhas):  
        colunas = len(matriz[i])
        for j in range(colunas):
            if j == colunas-1:
                print(matriz[i][j])
                break
            
            print(matriz[i][j], end=" ")
