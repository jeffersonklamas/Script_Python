#######################################################
# Desenvolvido por Jefferson Klamas
#
# Para aquele teste de lógica e/ou pensamento fluído
# Com tempo bem limitado
#
#######################################################

import os

# Limpando a tela
os.system('clear') or None

# Limpando variáveis
valor1 = 0
valor2 = 0
valor_media1 = 0
valor_total =0

# Inicio
print('Para responder perguntas sobre Cálculo de média')
print()
print('Exemplo de perguntas em teste de pensamento fluído:')
print()
print('          A idade média de A e B foi 85. \n          Se a média entre A, B e L é 90,\n          qual a idade de L?')
print()
print('Digite somente valores inteiros e sem os símbolos\n')

# Início do processo.
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

# Vamos tentar entender
print()
print('     Lembre: A média é dada pela soma dos elementos de um conjunto, \n     dividido pelo número de elementos do mesmo. ')
print()
print('     O primeiro valor é a média de idade de A e B, Então o cálculo é (A + B)/2 = 85')
print()
print('     Invertemos este cálculo para encontrarmos a soma das duas idades ((A + B) = 85 * 2) = 170')
print()
print('     Agora o segundo valor que é (A + B + L)/3 = 90')
print()
print('     Fazendo as substituições: ((170 + L) = 90 * 3) = (L = 270 - 170) = (L = 100)')
print()
print('     No exemplo acima a idade de L é 100')
print()
print()
print()
# Primeiro Cálculo
valor_media1 = (valor1 * 2)

# Resultado
valor_total = ((valor2 * 3) - valor_media1)

print('O RESULTADO DOS SEUS VALORES É: ', valor_total)
print('')
print('Boa sorte')