num = int(input('Digite um número com 5 digitos: '))
n = 0
nume = num
soma = 0
num1 = num % 10
num = num // 10

num2 = num % 10
num  = num //10

num3 = num % 10
num = num // 10

num4 = num % 10
num = num // 10

num5 = num

if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
    print('um digito se repete mais de 2 vezes')
elif num2 == num3 or num2 == num4 or num2 == num5:
    print('um digito se repete mais de 2 vezes')
elif num3 == num4 or num3 == num5:
    print('um digito se repete mais de 2 vezes')
elif num4 == num5:
    print('um digito se repete mais de 2 vezes')
else:
    print('um digito não se repete mais de 2 vezes')