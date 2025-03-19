from random import randint
while True:
    numero = randint(1,9)
    escolha = 0
    while escolha != numero:
        escolha = int(input('Tente adivinhar um número entre 1 e 9: '))
        if escolha == numero:
            print('Você acertou! Parabéns!!')
        elif escolha > numero:
            print('Número é muito alto')
        else:
            print('Número é muito baixo')
    continuar = input('Deseja ficar [digite "ficar"] ou deseja sair [digite "sair"]? ')
    if continuar == 'sair':
        break
print('Fim de Jogo')