# Crie um programa para determinar se um número inteiro dado é maior que 10 e menor que 20, ou se é maior que 30 ou menor que 5. Utilize uma única linha de código dentro de cada bloco 'if' e 'else' para imprimir "maior que 10 e menor que 20", "maior que 30 ou menor que 5" ou "não é maior que 10 e menor que 20 e não é maior que 30 ou menor que 5"

num = int(input('Digite um número: '))

if num > 10 and num < 20:
    print('Maior que 10 e menor que 20')
elif num > 30 or num < 5:
    print('Maior que 30 ou menor que 5')
else: 
    print('Não é maior que 10 e menor que 20 e não é maior que 30 ou menor que 5')