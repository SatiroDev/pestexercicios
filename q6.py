#Crie um programa para ler um número de 5 dígitos e verifique se existe algum dígito que se repete 2 ou mais vezes.
#OBS: NÃO converta Npara string. Trate-o como número!

num = 56743
nume = num
num1 = num % 10
numer = 1
num = num // 10
num2 = num % 10

num = num // 10
num3 = num % 10

num = num // 10
num4 = num % 10

num = num // 10
num5 = num % 10

if num1 in nume:
    num +=1
print(num)