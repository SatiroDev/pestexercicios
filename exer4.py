hora_atual = int(input('Hora atual: '))
temp_alarme = int(input('Daqui quantas horas quer que o alarme toque? '))
horario_do_alarme = (hora_atual + temp_alarme) % 24
print(f'O alarme ira tocar as {horario_do_alarme} horas')