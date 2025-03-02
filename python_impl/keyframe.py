import csv
class CSVKeyframe:
    #stored as time_frame , start node, angles[]
    real_time_update = False
    default_start_node_idx = 0

    def __init__(self,file_path="keyframe.csv"):
        #load csv 
        self.file_path = file_path
        self.data = []
        with open(self.file_path, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        self.data = data
        #self.data = [float(x) for x in data]
        self.current_write_frame = 0

    def read(self,frame=0,address= 0)->float:
        return float(self.data[frame][address])

    def write(self,frame= 0, address = 0):    
        self.current_frame = frame
        #if current_frame is bigger than data list size
        if self.current_frame > len(data):
            self.data.append(self.)
        self.data[self.current_write_frame][address] =  

    def write_end(self):
        # Write lines to CSV file
        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in self.data:lu
                writer.writerow(line)

    def make_new_keyframe(self):
        keyframe = [0]*len(data)-1 
        keyframe[0] = self.current_frame
        keyframe[1] = self.default_start_node_idx
        return (keyframe)


if __name__ == "__main__":
    keyframe = CSVKeyframe("/media/ducktop/shared/code/cpp/Jointgraph/resources/keyframe.csv")
    print(float(keyframe.data[0][1]))
