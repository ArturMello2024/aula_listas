import math
def somatorio(n):
    soma = 0
    for i in range(1, n+1):
        soma += math.pow((i+1),2)
    return soma

n = int(input("Insira um valor"))
resultado = somatorio(n)
print(resultado)