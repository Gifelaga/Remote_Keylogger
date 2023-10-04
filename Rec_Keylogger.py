import socket
import threading
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

super_secret_key = b'super_secret_key'
cipher = AES.new(super_secret_key, AES.MODE_ECB)

HOST = 'localhost'
PORT = 6969

def handle_client(client_socket):
    log = ''
    while True:
        try:
            log += unpad(cipher.decrypt(client_socket.recv(1024)[:-1]), 16).decode()
            with open('log.txt', 'w') as f:
                f.write(log)
        except:
            pass

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print('Server listening on {}:{}'.format(HOST, PORT))

    while True:
        client_socket, addr = server.accept()
        print('Accepted connection from {}:{}'.format(addr[0], addr[1]))
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()
