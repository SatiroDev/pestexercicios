# Escreva uma função chamada intercalar_letrasque aceite duas strings como entrada e retorne uma nova string contendo as letras intercaladas das duas strings, ou seja, a primeira letra da primeira string, a primeira letra da segunda string, a segunda letra da primeira string e assim por diante.

# Ex: intercalar_letras("Olá", "Mundo!")deve retornar"OMluándo!”

def intercalar_letras(string1: str, string2: str):
    qnt_string1 = len(string1)
    qnt_string2 = len(string2)
    nova_string = ''
    if qnt_string1 >= qnt_string2:
        for i in range(qnt_string2):
            nova_string += string1[i:i+1]
            nova_string += string2[i:i+1]
    else: 
        for i in range(qnt_string2):
            nova_string += string1[i:i+1]
            nova_string += string2[i:i+1]
    nova_string_final = nova_string + string1[qnt_string2:]
    return nova_string_final

palavra_1 = input('Digite uma palavra: ')
palavra_2 = input('Digite outra palavra: ')
print(intercalar_letras(palavra_1, palavra_2))