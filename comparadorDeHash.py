# Gerador de hash

import hashlib
import os

os.system('clear') or None

arq1 = '/home/jkm/Learning/Script_Python/Arquivos/a.txt'
arq2 = '/home/jkm/Learning/Script_Python/Arquivos/b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arq1, 'rb').read()) 

hash2 = hashlib.new('ripemd160')

hash2.update(open(arq2, 'rb').read()) 

if hash1.digest() != hash2.digest():
	print(f'O arquivo: {arq1}  é diferente do arquivo: {arq2}')
	print('O hash do arquivo a.txt é: ', hash1.hexdigest())
	print('O hash do arquivo a.txt é: ', hash2.hexdigest())
else:
	print(f'O arquivo: {arq1}  é igual ao arquivo: {arq2}')
	print('O hash do arquivo a.txt é: ', hash1.hexdigest())
	print('O hash do arquivo a.txt é: ', hash2.hexdigest())

