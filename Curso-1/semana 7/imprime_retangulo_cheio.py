
l = int(input("digite a largura:"))
a = int(input("digite a altura:"))


while a > 0:
	p=0
	while l > 0 and p < l:
		print("#", end="")
		p += 1
	a -= 1
	print("")