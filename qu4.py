num = int(input('Digite um número: '))
nume = num
copia_num = num
inverso = 0
quantidade_digs = 0
cont = 1
while nume:
    nume //= 10
    quantidade_digs += 1

while cont <= quantidade_digs:
    inverso = inverso * 10 + num % 10
    num //= 10
    cont += 1

print(f'Número normal {copia_num}, número ao contrário {inverso}')