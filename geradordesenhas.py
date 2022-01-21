# Gerador de senhas

import random
import string
import os

os.system('clear') or None

tamanho = int(input('Digite o tamanho de senha que você precisa: '))

chars = string.ascii_letters + string.digits + 'ç!@#$%&*(?)_+"'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
