import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('\033[32mCliente Socket criado com sucesso!\033[m')

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor, como está?'

try:
    #print('Cliente: {}'.format(mensagem))
    s.sendto(mensagem.encode(), (host,5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('\033[33mCliente\033[m: {}'.format(dados))
finally:
    print('\033[31mCliente: Fechando a conexão\033[m')
    s.close()

