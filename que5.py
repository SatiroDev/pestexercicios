num = int(input('Digite um número: '))
c = 0
for i in range(1, num+1):
    if num % i == 0:
        c += 1
if c == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')
