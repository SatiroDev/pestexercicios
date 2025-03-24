num = int(input('Digite um número: '))
soma = 0
quantidade = 0
for i in range(0, num+1):
    soma += i
    quantidade += 1
print(f'A média foi de {soma/quantidade}')