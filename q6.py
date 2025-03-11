num = 55550
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
n1 = 0
if num1 == num2:
    n += 3
    n1 += 1
    soma += num1
else:
    if num1 == num3:
        n += 3
        n1 += 1
        soma += num1
    else:
        if num1 == num4:
            n += 3
            n1 += 1
            soma += num1
        else:
            if num1 == num5:
                n += 3
                n1 += 1
                soma += num1

if num2 == num3:
    n += 3
    n1 += 1
    soma += num2
else:
    if num2 == num4:
        n += 3
        n1 += 1
        soma += num2
    else:
        if num2 == num5:
            n += 3
            n1 += 1
            soma += num2

if num3 == num4:
    n += 3
    n1 += 1
    soma += num3

else:
    if num3 == num5:
        n += 3
        n1 += 1
        soma += num3

if num4 == num5:
    n += 3
    n1 += 1
    soma += num4
numeri = soma / n1

print(numeri)
if numeri >= 2:
    print('um digito se repete mais de 2 vezes')
else:
    print('um digito não se repete mais de 2 vezes')