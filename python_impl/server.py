import socket
import yaml
import yamlLoader as yl
import byteStreamHandler as BSH
import time
class Server:
    subscriber_addresses = []
    server_ok = 200
    def __init__(self,server_ip="",server_port=8080):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_info = (server_ip,server_port)
        self.server_socket.bind(self.server_info)
        self.encoder = BSH.ByteStreamHandler()

    
    def get_subscribers(self):
        port, address = self.server_socket.recvfrom(1024)
        #print(port)
        #print(int.from_bytes(port,'little'));
        #print(address)
        self.subscriber_addresses.append((address[0],int.from_bytes(port,'little')))
        print(self.subscriber_addresses[-1])
        #self.server_socket.sendto(bytes(512),('127.0.0.1',8080))
        self.server_socket.sendto(self.server_ok.to_bytes(1,'little'),self.subscriber_addresses[-1])

    def publish_int_array(self,data_to_send):
        msg_to_send = self.encoder.compose_byte_frame(data_to_send)
        print((msg_to_send,"sent"))
        for client_tuple in self.subscriber_addresses:
            self.server_socket.sendto(msg_to_send,client_tuple)


        

if __name__ == "__main__":

   # ('', yl.dictionary['server']['port']))
    controller = Server(yl.dictionary['server']['ip'],yl.dictionary['server']['port'])
    controller.get_subscribers()
    time.sleep(5)
    data_to_send = [0,134,247,39,40,52]
    for i in range(0,20):
        controller.publish_int_array(data_to_send)
   # byte_encoder = BSH.ByteStreamHandler()
    

    #msg = byte_decoder.decompose_byte_frame(message)
    #print((msg,address))



