num = int(input('Digite um número: '))

pares = 'Número não é par'
impares = 'Número não é impar'
if num == 0:
    print('Neutro')
elif num % 2 == 0:
    pares = num
else:
    impares = num

print(pares)
print(impares)

