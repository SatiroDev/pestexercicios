#Crie um programa para determinar se um número inteiro dado é divisível por 2, 3 ou nenhum deles. Utilize uma única linha de código dentro de cada bloco 'if', 'elif' e 'else' para imprimir "divisível por 2", "divisível por 3" ou "não é divisível por 2 ou 3" respectivamente."

num = int(input('Digite um número: '))
if num % 2 == 0:
    print('Divisível por 2')
elif num % 3 == 0:
    print('Divisível por 3')
else:
    print('Não é divisível por 2 ou 3')
