

def soma_matrizes(m1, m2):

	linhas = len(m1)
	colunas = len(m1[0])

	if linhas != len(m2) or colunas != len(m2[0]):
		return False

	soma = m1[:]

	for i in range(linhas):  
	    for j in range(colunas):
	        soma[i][j] = m1[i][j] + m2[i][j]

	return soma
