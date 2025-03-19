num_binario = int(input('Digite um número binário: '))
nume = num_binario
copia_bin = num_binario
quant_digs = -1
decimal = 0
while nume:
    nume //= 10
    quant_digs += 1
cont = 0
while cont <= quant_digs:
    mult = (num_binario % 10 * (2**cont))
    num_binario //= 10
    decimal += mult
    cont += 1
print(f'{copia_bin} binarios corresponde ao número decimal -> {decimal}')