largura = int(input("digite a largura:"))
altura = int(input("digite a altura:"))

a = altura
l = largura

while a > 0:
	p=0
	while l > 0 and p < l:
		if p == 0 or p == (l-1):
			print("#",end="")
		else:
			if a == 1 or a == altura:
				print("#", end="")
			else:
				print(" ", end="")
		p += 1
	a -= 1
	print("")