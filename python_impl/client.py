#place on pupet
import socket
import yamlLoader as yl


if __name__ == "__main__":
    msg = 5 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ls = {2,3,4,5}
    #msg2send = msg.to_bytes(ls, 'big')
    msg2send = bytearray(ls)
    print(msg2send.decode("utf-8"),"sent")
    client_socket.sendto(msg2send, (yl.dictionary['server']['ip'],yl.dictionary['server']['port']))

    