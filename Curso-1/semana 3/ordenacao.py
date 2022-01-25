numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if (numero1 > numero2) or (numero2 > numero3):
	print("não está em ordem crescente")
else:
	print("crescente")