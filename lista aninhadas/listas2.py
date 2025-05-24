# Crie um programa que permita ao usuário registrar informações de alunos, incluindo nome, idade e notas em diversas disciplinas. Use uma lista aninhada para representar os alunos, onde cada aluno é uma lista com seu nome, idade e uma lista de notas. O programa deve permitir adicionar novos alunos, remover alunos existentes e calcular a média de notas de cada aluno.

alunos = []

def menu():
    print('1. Adicionar aluno')
    print('2. Remover aluno')
    print('3. Mostrar alunos com média')
    print('4. Sair')
    escolha = input('Escolha uma opção: ')
    return escolha

def adicionar_aluno():
    nome_aluno = input('Nome do aluno: ')
    idade_aluno = int(input(f'Idade do(a) aluno(a) "{nome_aluno}": '))
    quant_notas = int(input('Quantas notas do aluno? '))
    notas = []
    for i in range(quant_notas):
        nota = float(input(f'Nota {i+1}: '))
        notas.append(nota)
    alunos.append([nome_aluno, idade_aluno, notas])

def remover_aluno():
    if alunos != []:
        for aluno in alunos:
            print(aluno[0])
        nome_aluno_remocao = input('Nome do aluno que deseja remover: ')
        verificacao = False
        for aluno in alunos:
            if aluno[0] == nome_aluno_remocao:
                verificacao = True
                alunos.remove(aluno)
                print(f'Aluno "{nome_aluno_remocao}" removido com sucesso!')
                break
        if verificacao == False:
            print(f'Aluno "{nome_aluno_remocao}" não encontrado!')
    else:
        print('Nenhum aluno adicionado!')


def mostrar_alunos():
    if alunos != []:
        for aluno in alunos:
            print(f'Nome: {aluno[0]}')
            print(f'Idade: {aluno[1]}')
            print(f'Notas: {alunos[2]}')
            print(f'Média: {sum(alunos[2])/ len(alunos[2]):.2f}')
    else:
        print('Nenhum aluno adicionado!')
    

while True:
    opcao = menu()
    if opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        remover_aluno()
    elif opcao == '3':
        mostrar_alunos()
    elif opcao == '4':
        print('Fim do programa!')
        break
    else:
        print(f'Opção "{opcao}" inválida!')