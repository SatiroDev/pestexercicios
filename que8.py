n = int(input('Digite um número: '))
for i in range(1, n+1):
    fatorial = 1
    for c in range(i, 0, -1):
        fatorial *= c
    print(f'{i}! = {fatorial}')