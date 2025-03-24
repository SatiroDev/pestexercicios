for i in range(1, 2):
    i = 10
    copia = i
    quantidade = 0
    for c in range(0, i):
        quantidade += 1
        i //= 10 
    print(quantidade)