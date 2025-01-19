#place on pupet
import socket
import yamlLoader as yl
import byteStreamHandler as BSH

class Client:

    def __init__(self,server_ip="127.0.0.1",server_port=8080,client_port= 8888):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_port = client_port
        self.client_socket.bind(('',self.client_port))

    def subscribe(self,server_ip= "127.0.0.1",server_port=8080):
        #subscribe
        server_info = (server_ip,server_port)
        self.client_socket.settimeout(10)
        isNotConnected=True
        while(isNotConnected):
            self.client_socket.sendto(self.client_port.to_bytes(2,'little'),server_info)
            message,address = self.client_socket.recvfrom(1024)
            response_code = int.from_bytes(message,'little') 
            isNotConnected = response_code != 200
            print(response_code==response_code)

        self.byte_decoder = BSH.ByteStreamHandler()



    def send_int_array(self,data_to_send):
        msg2send = self.byte_encoder.compose_byte_frame(data_to_send)
        #self.client_socket.sendto(msg2send, )
        pass

if __name__ == "__main__":
    
   
    #(yl.dictionary['server']['ip'],yl.dictionary['server']['port'])
    puppet = Client(yl.dictionary['client']['port'])
    puppet.subscribe(server_ip= yl.dictionary['server']['ip'], server_port = yl.dictionary['server']['port'])
    print("sent")
    

    
