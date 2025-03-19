# num_dec = int(input('Digite um número binário: '))
# nume = num_dec
# quant_digs = -1
# soma = 0
# while nume:
#     nume //= 10
#     quant_digs += 1
# cont = 0
# while cont <= quant_digs:
#     mult = (num_dec % 10 * (2**cont))
#     num_dec //= 10
#     soma += mult
#     cont += 1
# print(soma)

num_dec = int(input('Digite um número binário: '))
nume = num_dec
quant_digs = -1
soma = 0
c = 1
bii = 0
while num_dec/2 == 0:
    bina = num_dec % 2 
    soma = bina + bii * 10
    bii = bina
    num_dec /= 2
    c += 1
print(soma)

