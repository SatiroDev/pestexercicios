#Escreva um programa para verificar se um número de três dígitos é um palíndromo.
#Ex: 101, 111, ...
#OBS: NÃO converta N para string. Trate-o como número!

num = 111
nume = num


inv = 0
inv = inv * 10 + num % 10
num //= 10
inv = inv * 10 + num % 10
num //= 10
inv = inv * 10 + num % 10

if inv == nume:
    print(f'O número {nume} é palíndromo!')
else:
    print(f'O número {nume} não é palíndromo!')
