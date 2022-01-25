def ordenada( lista ):
	for i in range(len(lista)-1):
		if lista[i] < lista[i+1]:
			continue
		return False

	return True
