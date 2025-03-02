horas_atual = 2
alarme_temp = 51
alarmar = (alarme_temp + horas_atual) % 24
print(f'horário atual é {horas_atual}, botar uma alarme para alarmar daqui a {alarme_temp}, ele ira alarmar as {alarmar} horas')