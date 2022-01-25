

''' Multiplica se numero de colunas da primeira matriz 
	eh igual ao numero de linhas da segunda matriz '''
def sao_multiplicaveis(m1, m2):
	if len(m1[0]) == len(m2):
		return True

	return False


m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(sao_multiplicaveis(m1, m2))

m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
print(sao_multiplicaveis(m1, m2))