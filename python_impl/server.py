import socket
import yaml
import yamlLoader as yl
import byteStreamHandler as BSH

class Server:
    subscriber_addresses = []
    def __init__(self,server_ip="",server_port=8080):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_info = (server_ip,server_port)
        self.server_socket.bind('',self.server_info)
    
    def get_subscribers(self):
        port, address = self.server_socket.recvfrom(1024)
        print(port)
        self.subscriber_addresses.append((address[0],int.from_bytes(port)))

        self.server_socket.send(bytes('ok'),self.subscriber_addresses[0])



if __name__ == "__main__":

    ('', yl.dictionary['server']['port']))
    byte_encoder = BSH.ByteStreamHandler()

    data_to_send = [0,134,247,39,40,52]

    msg = byte_decoder.decompose_byte_frame(message)
    print((msg,address))



