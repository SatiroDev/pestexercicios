n = int(input('Digite um número: '))
for i in range(0, n+1):
    fatorial = 0
    for c in range(i, 0, -1):
        fatorial *= c
    print(f'{i}! = {fatorial}')