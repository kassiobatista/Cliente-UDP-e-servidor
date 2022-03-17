import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso!')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = '\n\033[35mServidor\033[m: Olá cliente, tudo bem ?'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + mensagem.encode(), end)
