# Exercite seus conhecimentos, crie um programa capaz de consultar um nome de domínio e obtenha através de uma conexão HTTP, conteúdos on-line e, de acordo com o tipo do conteúdo, imprima na tela uma ação diferente.

# Crie uma função em python3 que utilize a biblioteca:

# import http.client
# A função deve ter o cabeçalho e os parâmetros definidos como:

# def HTTPclient(host,port)
# Onde os parâmetros "host" é um endereço IP informado como string e "port" é um inteiro com a porta onde o serviço de rede para páginas web está hospedado. Ambos os parâmetros não precisam ser recebidos por entrada de dados, a rotina principal irá instanciá-los, o esforço deve ser único e exclusivamente desempenhado para criar a função HTTPclient().

# Dica:
# Utilize a função oriunda da classe HTTPResponse, getheaders() (https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse) para se obter o cabeçalho da mensagem HTTP.

# Exemplo:

# conn = http.client.HTTPConnection(host, port)

# conn.request("GET",content)

# r1 = conn.getresponse()

# data1 = r1.getheaders()       

# Para realizar esse exercício, consulte a RFC "Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content" em https://tools.ietf.org/html/rfc7231#section-3.1.1.5

# Entrada

# O programa receberá uma variável inteira L ([[1 \le L \le 20]]) informando o total de conteúdos a serem consultados. A seguir, vários nomes de conteúdos a serem obtidos serão fornecidos ao programa, os quais deverão ser consultados 1 à 1 e imprimir na tela comandos a serem executados de acordo com o tipo obtido.

# Saída

# Um comando para cada um dos conteúdos consultados deverá ser impresso na tela, onde, para a variável contendo o conteúdo $conteúdo e de acodo com o tipos de conteúdo, a seguinte :

# Tipo	Mensagem
# audio/mpeg	Playing audio: $conteúdo
# text/html	Browsing: $conteudo
# video/x-msvideo	Playing media: $conteudo
# application/json	Processing JSON: %s
# Formato desconhecido	Unknown file/media: $tipo_conteudo-$conteudo
# Conteúdo indisponível	Content not found
# Tipo de conteúdo e ações a serem executadas


# For example:

# Input	Result
# 5
# index.html
# content.json
# media.avi
# music.mp3
# this_does_not_exist
# Browsing: index.html
# Processing JSON: content.json
# Playing media: media.avi
# Playing audio: music.mp3
# Content not found

import http.client

content_type = {
    "audio/mpeg": "Playing audio:",
    "audio/mp3": "Playing audio:",
    "text/html": "Browsing:",
    "video/x-msvideo": "Playing media:",
    "video/avi": "Playing media:",
    "application/json": "Processing JSON:",
}

def HTTPclient (host, port):
	conn = http.client.HTTPConnection(host, port)
	
	L = int(input())
	if L not in range(1,21):
		raise Exception("L is not in range(1,21)")

	for i in range(L):
		url = input()
		conn.request("GET", url)
		
		r1 = conn.getresponse()
		if r1.status == 404:
			print("Content not found")
			continue

		data1 = r1.getheaders()
		for j in range(len(data1)):
			if str(data1[j][0]).lower() == "content-type":
				message = content_type.get(data1[j][1], "Unknown file/media:")

				filename = url.split("/")
				if message == "Unknown file/media:":
					content = data1[j][1] + "-" + filename[len(filename)-1]
				else:
					content = filename[len(filename)-1]

				print(message, content)
				break

	conn.close()
