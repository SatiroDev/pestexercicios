soma = 0
for i in range(1, 101):
    c = 0
    for cont in range(1, 101):
        if i % cont == 0:
            c += 1
    if c == 2:
        print(i)
        soma += i
print(f'A soma foi de {soma}')