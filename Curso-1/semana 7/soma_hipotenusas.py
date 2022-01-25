import math

def é_hipotenusa(n):
    a = 1
    while a <= n:
        b = 1
        while b <= n:
            c = int(math.sqrt((a ** 2) + (b ** 2)))

            if (c > a) and (c > b) and (c < (a + b)):
                if (a ** 2) + (b ** 2) == c ** 2:
                    if c == n:
                        return c
            b += 1
        a += 1

    return 0

def soma_hipotenusas(n):
    i = 1
    soma = 0
    valor_anterior = 0

    while i <= n:
        valor = é_hipotenusa(i)
        if valor != valor_anterior:
            soma += valor

        valor_anterior = valor 
        i += 1

    return soma

print(soma_hipotenusas(25))