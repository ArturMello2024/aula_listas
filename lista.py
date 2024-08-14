#crie uma lsita com 1000 elementos e calculel a media da lista, utilizando apenas funções
# modo 1
lista1 = []
n= 1000

for i in range (n):
    lista1.append(i)
x = sum(lista1) / len(lista1)
print(x)


# modo 2
lista = list(range(1, 1001))
for i in lista:
    media = sum(lista) / len(lista)
print(media)

