num = int(input('Digite um número positivo: '))
copia_num = num
copia_num1 = num
numer = num
quant_digs = 0
soma = 0
while numer:
    numer //= 10
    quant_digs += 1
while num > 0:
    copia_num1 = num % 10
    mult = copia_num1 ** quant_digs
    soma += mult
    num //= 10
if copia_num == soma:
    print(f'O número {copia_num} é Armstrong')
else:
    print(f'O número {copia_num} não é Armstrong')