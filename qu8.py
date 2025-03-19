num_binario = int(input('Digite um número binário: '))
nume = num_binario
quant_digs = -1
soma = 0
while nume:
    nume //= 10
    quant_digs += 1
cont = 0
while cont <= quant_digs:
    mult = (num_binario % 10 * (2**cont))
    num_binario //= 10
    soma += mult
    cont += 1
print(soma)