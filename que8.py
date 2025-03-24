# n = int(input('Digite um número: '))
# fatorial = 1
# mult = 0
# for i in range(1, n+1):

#     print(n)
#     fatorial *= n
#     n -= 1
# print(fatorial)
    
        
n = int(input('Digite um número: '))

for i in range(1, n+1):
    fatorial = 1
    for c in range(i, 0, -1):
        fatorial *= c
    print(f'{i}! = {fatorial}')
    