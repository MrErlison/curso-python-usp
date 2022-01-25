
numero = int( input("Digite o valor: ") ) 
soma = 0

while numero > 0:
    soma += numero % 10
    numero = numero // 10
    
print(soma)
