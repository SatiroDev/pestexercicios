inicio = int(input('Número para ser o inicial: '))
fim = int(input('Número para ser o ultimo: '))
for i in range(inicio, fim+1):
    copi = i
    copia = i
    copia2 = i
    quantidade = 0
    soma = 0
    for c in range(0, i):
        i //= 10
        quantidade += 1
        if i == 0:
            for cont in range(1, copi+1):
                copia = copia2 % 10
                mult = copia ** quantidade
                soma += mult
                copia2 //= 10
    if copi == soma:
        print(f'O número {copi} é Armstrong')
