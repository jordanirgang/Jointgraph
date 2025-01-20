import time
import math
def get_processed_timestamp():
    #return only minutes
    return int((time.time()%1000)/100)

class ByteStreamHandler:
    endian = 'little'
    is_positive = True
    droped_frames = 0
    def __init__(self):
        # a byte has 8 bits which adds ip uy\\
        self.max_frame = 65532#16777215
        self.time_start = get_processed_timestamp()
        self.frame = 1
        self.prev_frame = 0
        self.byte_components = 2

    def inc_frame(self):
        if self.is_positive:
            self.frame +=1
        else:
            self.frame -=1
        
    def get_frame(self)->bytes:
        bytes_out = self.frame.to_bytes(self.byte_components,self.endian)
        return bytes_out
    
    def compose_byte_frame(self,int_array_in:list)->bytearray:
        #format is frame,timestamp,start_pos,array
        timestamp = abs(get_processed_timestamp() - self.time_start)  #sending as minutes elapsed

        if self.frame >= self.max_frame or self.frame<= 0:
            self.is_positive = not self.is_positive
        self.inc_frame()
        byte_list = bytearray(self.get_frame())
        #print(timestamp)
        byte_list.append(timestamp)
        for i in int_array_in:
            byte_list.append(i)
        #print (byte_list)
        return byte_list

    def decompose_byte_frame(self,byte_array_in):
        frame_bytes = byte_array_in[0:self.byte_components]
        
        int_array_out = list(byte_array_in)
        for i in range(0,self.byte_components):
            int_array_out.pop(0)
        minute_check = int_array_out.pop(0)

        decomposed_frame = int.from_bytes(frame_bytes, self.endian)
        #seq mechanism 1 check if packet sent within the same minute
        if minute_check == abs(get_processed_timestamp() - self.time_start):
        #seq mechanism 2 drop all left over packets, will drop everything if frame count resets
                if (self.is_positive and decomposed_frame >= self.prev_frame) or (
                    not self.is_positive and decomposed_frame <= self.prev_frame):
                    #print(('frame in',decomposed_frame))
                    self.prev_frame = decomposed_frame 
                    return int_array_out
        self.droped_frames +=1
        print((self.frame,int_array_out,"dropped"))
        return []


if __name__ == "__main__":
    test = ByteStreamHandler()
    ray = [0,134,247,39,40,52]
    test.get_frame()
    time_start = time.time()

    print(time.time())
    for i in range(0,16777215):
        #print (test.compose_byte_frame(ray))
        simulated_packet = test.compose_byte_frame(ray)
        #test.decompose_byte_frame(simulated_packet)
        print (test.decompose_byte_frame(simulated_packet))
    #my issue is that there is a max number of frames able to be counted 
    print("********************")
    print(time.time() - time_start)

