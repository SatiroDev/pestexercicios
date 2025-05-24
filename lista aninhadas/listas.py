# Crie uma lista de listas com 3 elementos em cada e mostre um elemento a elemento dessa lista de listas.

lista = [[1, 2, 3], [11, 22, 33], [111, 222, 333]]

for elementos in lista:
    for elemento in elementos:
        print(elemento)
    print('-='*5)