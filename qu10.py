print('Encontrar todos os números de Armstrong dado um intervalo')
comecar = int(input('Digite o número para começar: '))
fim = int(input('Digite um número para finalizar: '))
print(f'Os números Armstrong entre {comecar} e {fim} são: ')
while True:
    quant_digs = 0 
    soma = 0
    copia_c2 = comecar
    cc = comecar
    while copia_c2:
        copia_c2 //= 10
        quant_digs += 1
    copia_digs = quant_digs
    while copia_digs:
        copia_c1 = cc % 10
        mult = copia_c1 ** quant_digs
        soma += mult
        cc //= 10
        copia_digs -= 1
    if comecar == soma:
        print(comecar)
    if comecar == fim:
        break
    comecar += 1