# Crie um código em Python que parte do usuário para digitar um número inteiro positivo e, em seguida, utilize o comando "while" para imprimir cada número até chegar ao número digitado pelo usuário.


num = int(input('Digite um número positivo: '))
c = 1
while c <= num:
    print(c)
    c += 1
print('FIM')