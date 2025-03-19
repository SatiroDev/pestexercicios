while True:
    num = int(input('Digite um número [0 para parar]: '))
    c = num
    if num == 0:
        break
    else:
        while c != 0:
            if num % c == 0:
                print(c)
            c -= 1
    
