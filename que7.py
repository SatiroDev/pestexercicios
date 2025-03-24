soma = 0
for i in range(1, 101):
    c = 0
    for cont in range(1, 101):
        if i % cont == 0:
            c += 1
    if c == 2:
        soma += i
print(f'A soma dos números primos de 1 até 100 foi de: {soma}')