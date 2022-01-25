
lista = []
valor = int(input("Digite um número:"))
while valor != 0:
	lista.insert(0,valor)
	valor = int(input("Digite um número:"))

for x in lista:
	print(x)