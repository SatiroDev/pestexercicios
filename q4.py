soma = 0
num1 = int(input('Digite um número: '))
soma += num1
num2 = int(input('Digite um número: '))
soma += num2
num3 = int(input('Digite um número: '))
soma += num3
if num1 != num2 and num2 != num3 and num1 != num3:
    print(f'A soma dos números foi de {soma}')
else:
    print('Soma = 0')