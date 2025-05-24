# Crie um programa que peça ao usuário para especificar o número de linhas e colunas de uma matriz. Em seguida, preencha a matriz com números inteiros fornecidos pelo usuário. Use listas aninhadas para representar a matriz.

matriz = []

linhas = int(input('Digite quantas linhas você vai querer na matriz: '))

colunas = int(input('Digite quantas linhas você vai querer na matriz: '))

for i in range(linhas):
    linha = []
    for y in range(colunas):
        elemento = int(input(f'Digite um número para posição ({i+1}, {y+1}): '))
        linha.append(elemento)
    matriz.append(linha)

for linhas in matriz:
    print(linhas)