num = 1023
nume = num
soma = 0
if num:
    num = num // 1000
    soma += num
    nume = nume % 1000
    if nume:
        num = nume // 100
        soma += num 
        nume = nume % 100
        if nume:
            num = nume // 10
            soma += num
            nume = nume % 10
            if nume:
                num = nume / 1
                soma += num
print(soma)