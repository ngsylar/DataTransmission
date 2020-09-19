# Exercite seus conhecimentos, crie um programa capaz de consultar um nome de domínio e obtenha várias páginas web.

# Para isso, crie uma função em python3 que utilize a biblioteca:

# import http.client
# A função deve ter o cabeçalho e os parâmetros definidos como:

# def HTTPclient(host,port)
# Onde os parâmetros "host" é um endereço IP informado como string e "port" é um inteiro com a porta onde o serviço de rede para páginas web está hospedado. Ambos os parâmetros não precisam ser recebidos por entrada de dados, a rotina principal irá instanciá-los, o esforço deve ser única e exclusivamente desempenhado para criar a função HTTPclient().

# Dica:

# Utilize um conector como abaixo:

# conn = http.client.HTTPConnection(host, port)

# Entradas

# O programa receberá uma variável inteira L ([[1 \le L \le 20]]) informando o total de conteúdos a serem consultados. A seguir, vários nomes de conteúdos a serem obtidos serão fornecidos ao programa, o qual deverá consultá-los 1 à 1 e imprimir na tela seus conteúdos.

# Saída

# Os conteúdos de cada um dos arquivos consultados deverá ser impresso na tela após decodificados, para isso, utilize a função .decode() dos dados obtidos por um request.

# For example:

# Input	Result
# 1
# index.html
# <HTML>
#     <HEADER>
#         <TITLE>Teste</TITLE>
#     </HEADER>
#     <BODY>TD é demais</BODY>
# </HTML>
# Answer:(penalty regime: 10, 20, ... %)

import http.client

def HTTPclient (host, port):
	conn = http.client.HTTPConnection(host, port)
	
	L = int(input())
	if L not in range(1,21):
		raise Exception("L is not in range(1,21)")

	for i in range(L):
		url = input()
		conn.request("GET", url)
		page = conn.getresponse().read().decode()
		print(page)

	conn.close()
