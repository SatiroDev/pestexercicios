while True:
    num = c = int(input('Digite um número [0 para parar]: '))
    if num == 0:
        break      
    while c != 0:
        if num % c == 0:
            print(c)
        c -= 1
    
