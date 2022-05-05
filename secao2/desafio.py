nome = str('Artur')
idade = int(23)
altura = float(1.76)
peso = float(90)
ano_atual = int(2022)
data_nasc = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} e pesa {peso:.0f}kg.')
print(f'O IMC de {nome} é {imc:.2f}.') 
print(f'{nome} nasceu em {data_nasc}.')
