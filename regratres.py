###################################################
# Elaborado por Jefferson Klamas
#
# Usado naqueles testes com tempo bem pequeno.
#
###################################################

import os

# Limpando a tela
os.system('clear') or None

# Limpando variáveis
valor1 = 0
valor2 = 0
valor3 = 0
valorReal = 0
lucro = 0

# Inicio
print('Para responder perguntas sobre Regra de três simples')
print()
print('Exemplo de perguntas em teste de pensamento fluído:')
print()
print('          João vendeu sua bicicleta a 360 reais, o que era 80% do que ele havia pago. \n          Por quanto ele deveria ter vendido para ter um lucro de 20%?')
print()
print('Digite somente valores inteiros e sem os símbolos\n')

valor1 = int(input('Digite o primeiro valor da questão: '))
valor2 = int(input('Digite o valor da porcentagem: '))
valor3 = int(input('Digite o valor do lucro: '))

# Calculando o valor real
valorReal = (valor1 * 100) / valor2
print()
print("O valor pago foi R$", valorReal)
print()
print('Calculando o lucro....')
print()
lucro = (valorReal*(100 + valor3))/100
print()
print("O lucro é", lucro)
print()
print('Boa sorte!!!!')