number = input("Escolha entre 1 e 12?")
mounths = {'1': 'January',  '2':'February', '3':'March', '4':'April' , '5':'May', '6':'June', '7':'July', '8':'Agust', '9': 'September', '10': 'October', '11': 'November', '12':'December'}
print(mounths['11'])

#  Militantes do twitter não passarão!

ttpost = input('Deixe aqui a sua Militancia:')
if len(ttpost) >= 280:
     print('Limite de caracteres excedido.Twite não postado')
else :
      print('Twite postado')

# Doe sangue.

fichario1 = input('Nome:')
fichario2 = input('Idade:')
fichario3 = input('Peso:')
fichario4 = input('Dormiu por quantas horas?')

print(fichario1)

if fichario2 <= '16':
    print('Requisito não atendido.')

if fichario2 >= '69' :
    print('Requisito não atendido;')

if fichario3 <= '50' :
    print('Requisito não atendido.')

if fichario4 <= '6' :
    print('Requisito não atendido.')

print(f'Parabéns, {fichario1}. Você pode doar!')

# ATENÇÃO AVALIADOR A ATIVIDADE POSSUI UM ERRO LÓGICO,
# CUJO ERRO JÁ ESTÁ CORRIGIDO AQUI.

temperatura = int(input("Digite a temperatura:"))

if temperatura > 25:
    print("Oba! A PDA pode marcar a data")
elif temperatura > 15 and temperatura <= 25:
    print("Vamos! O que vale é a companhia")
else:
    print("Estará muito frio, não podemos alugar nessa data")

# Ferias do Tio Tiago

tempo_minimo = str(input("O Tiago trabalhou 12 meses completos? [S/N]")).lower().startswith('s')
disponibilidade = str(input("O Tiago tem disponibilidade para tirar férias entre dezembro e janeiro? [S/N]")).lower().startswith('s')

if tempo_minimo and disponibilidade:
    print("O Tiago pode tirar férias!")
else:
    print("O Tiago não pode tirar férias!")

