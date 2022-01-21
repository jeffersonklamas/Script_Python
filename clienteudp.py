####################################################################
# Desenvolvido por Jefferson Klamas em 16/01/2022                  #
# Como parte prática da aula de Segurança de Informação com Python #
# Ministrado pelo Instrutor: Bruno de Campos Dias                  #
# Vídeo disponibilizado na Digital Innovation One                  #
# Site: web.dio.me                                                 #
#                                                                  #
# Introdução a Socket e cliente TCP/UDP e Server                   #
# Desenvolvimento de um cliente servidor e UDP                     #
#                                                                  #
# Para o UDP só se importa o socket                                #
#################################################################### 

import socket
# import sys
import os

# Limpa tela
os.system('clear') or None

# Criando a conexão UDP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket criado com sucesso!!!')

host = 'localhost'
porta = 5433

mensagem = 'Olá servidor, tudo bem?!'

try:
	print('Cliente: ' + mensagem)
	s.sendto(mensagem.encode(), (host, 5432))

	dados, servidor = s.recvfrom(4096)
	dados = dados.decode()
	print('Cliente: ' + dados)
finally:
	print('Cliente: Fechando a conexão')
	s.closed()


