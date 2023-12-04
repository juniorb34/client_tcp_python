import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(60)

try:

    client.connect(("127.0.0.1", 6000))
    client.send(b'TEXTO\n')
    pacotes_recebidos = client.recv(100000).decode()
except:
    print("Ocorreu um erro!")