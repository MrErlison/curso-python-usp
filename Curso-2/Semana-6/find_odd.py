

def only_odd(L):
	return L[0:L[0]&1] + only_odd(L[1:]) if L else L


lista = [1,2,3,4,5,6,7,8,9,0]
print(only_odd(lista))