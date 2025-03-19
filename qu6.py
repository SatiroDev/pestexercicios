c = 1
while c <= 100:
    if c % 3 == 0 and c % 5 == 0:
        print(f'{c} = "FizzBuzz"')
    elif c % 3 == 0 and c % 5 !=0 :
        print(f'{c} = "Fizz"')
    elif c % 5 == 0:
        print(f'{c} = "Buzz"')
    c += 1