
def ehprimo(x):
	if x == 2:
		return True

	fator = 2
	while x % fator != 0 and fator <= x/2:
		fator += 1

	if x % fator == 0:
		return False
	
	return True


def n_primos(x):
	contador = 0
	while x >= 2:
		if ehprimo(x):
			contador += 1
		x -= 1

	return contador

