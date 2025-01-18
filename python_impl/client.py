#place on pupet
import socket
import yamlLoader as yl
import byteStreamHandler as BSH

class Client:

    def __init__(self,server_ip="127.0.0.1",server_port=8080,client_port= 8888):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_info = (server_ip,server_port)
        #subscribe
        isNotConnected=True
        while(isNotConnected):
            self.client_socket.sendto(bytes(client_port),self.server_info)

        self.byte_decoder = BSH.ByteStreamHandler()

    def send_int_array(self,data_to_send):
        msg2send = self.byte_encoder.compose_byte_frame(data_to_send)
        self.client_socket.sendto(msg2send, )


if __name__ == "__main__":
    
   
    #(yl.dictionary['server']['ip'],yl.dictionary['server']['port'])
    print("sent")
    

    
