capa_livro = 24.95
valor_com_desc = capa_livro - (capa_livro * (40/100))
transporte = 3
copias = 60
valor_final = valor_com_desc * copias + (transporte + ((copias-1) * 0.75))
print(f'O custo total para {copias} copias é {valor_final:.2f}R$')
