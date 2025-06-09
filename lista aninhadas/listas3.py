# Implemente o jogo da velha (Tic-Tac-Toe) usando uma matriz 3x3 representada por uma lista aninhada. Permita que dois jogadores joguem alternadamente e verifiquem se alguém ganhou o jogo. O programa deve exibir o tabuleiro após cada jogo e informar o vencedor ou se houve um empate.
from random import randint
jogador = randint(1,2)

velha = [['','',''],['','',''],['','','']]
print('Escolha jogador 1 ou jogador 2')
while True:
    linha = int(input(''))