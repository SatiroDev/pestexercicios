for i in range(1, 1000):
    copi = i
    copia = i
    copia2 = i
    quantidade = 0
    soma = 0
    for c in range(0, i):
        i //= 10
        quantidade += 1
        if i == 0:
            for cont in range(1, copi+1):
                copia = copia2 % 10
                mult = copia ** quantidade
                soma += mult
                copia2 //= 10
    if copi == soma:
        print(f'O número {copi} é Armstrong soma = {soma}')
   

# num = int(input('Digite um número positivo: '))
# copia_num = num
# copia_num1 = num
# numer = num
# quant_digs = 0
# soma = 0
# while numer:
#     numer //= 10
#     quant_digs += 1
# while num > 0:
#     copia_num1 = num % 10
#     mult = copia_num1 ** quant_digs
#     soma += mult
#     num //= 10
# if copia_num == soma:
#     print(f'O número {copia_num} é Armstrong')
# else:
#     print(f'O número {copia_num} não é Armstrong')