import socket
import yaml
import yamlLoader as yl


if __name__ == "__main__":

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', yl.dictionary['server']['port']))

    message, address = server_socket.recvfrom(1024)
    msg = list(message)
    print((msg,address))



