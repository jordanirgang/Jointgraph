import time

def get_processed_timestamp():
    return int((time.time() %10000)*10 )

class ByteStreamHandler:
    def __init__(self):
        self.max_frame = 254
        self.frame = 0


    def compose_byte_frame(self,int_array_in:list)->bytearray:
        #format is timestamp,frame,start_pos,array
        timestamp = get_processed_timestamp()
        #int_array_in.insert(0,timestamp)
        int_array_in.insert(0,self.frame)
        if self.frame >self.max_frame:
            self.frame = 0
        else:
            self.frame +=1
        #print (int_array_in)
        return bytes(int_array_in)

    def decompose_byte_frame(self,byte_array_in):
        int_array_out = list(byte_array_in)
        int_array_out.pop(0)
        return int_array_out



if __name__ == "__main__":
    test = ByteStreamHandler()
    ray = [0,134,247,39,40,52]
    print (test.compose_byte_frame(ray))
    simulated_packet = test.compose_byte_frame(ray)
    print (test.decompose_byte_frame(simulated_packet))

