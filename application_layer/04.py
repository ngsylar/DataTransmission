# Crie um trecho de código capaz de receber vários IPs e realizar uma consulta a um sistema de nomes (Domain Name System) da internet. A partir da consulta, recupere os nomes de domínios (Domain Names) dos IPs acessados e imprima-os na tela. 

# Utilize a biblioteca socket e a função socket.gethostbyaddr().

# Entradas
# Você receberá uma variável inteira L=(0≤L≤10000) com o número de IPs a serem consultados. Em seguida, o programa deverá receber uma lista de IPs separados linha a linha.

# Saída

# Você deverá imprimir na tela os nomes de domínio (domain names) ligados aos IPs de entrada.

# *Obs.: Para entrar com um inteiro, utilize
# qualquer_variavel = int(input())

# For example:

# Input	Result
# 4
# 143.54.2.20
# 143.54.11.34
# 200.160.2.3
# 200.160.4.2
# www.ufrgs.br
# www.inf.ufrgs.br
# registro.br
# cgi.br
# Answer:(penalty regime: 10, 20, ... %)

import socket

L = int(input())
if L not in range(0,10001):
    raise Exception("L is not in range(0,10001)")

dns = []
for i in range(L):
    ip = input()
    domain = socket.gethostbyaddr(ip)
    dns.append(domain[0])

for domain in dns:
    print(domain)
