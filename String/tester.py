N = 10
soma = 0
for i in range(N+1):
    if i % 2 == 0:
        soma -= i
    else:
        soma += i
print(soma)