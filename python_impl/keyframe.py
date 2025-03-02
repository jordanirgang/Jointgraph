import csv
class CSVKeyframe:
    #stored as time_frame , start node, angles[]
    real_time_update = False
    default_start_node_idx = 0

    def __init__(self,file_path=""):
        #load csv 
        #self.data = [float(x) for x in data]
        self.current_write_frame = 0
        self.data = []
        if file_path:
            self.load_csv(file_path)
            

    def load_csv(self,file_path):
        self.file_path = file_path
        data = []
        try:
            with open(self.file_path, newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
        except:
            print("no file found")
        self.data = data

        

    def read(self,frame=0,address= 0)->float:
        return float(self.data[frame][address])

    def write(self,joint_angle, address = 0):    
        #print(len(self.data))
        #if current_frame is bigger than data list size
        if self.current_write_frame > len(self.data)-1:
            self.data.append(self.make_new_keyframe())

        self.data[self.current_write_frame][address] =  joint_angle
        self.current_write_frame +=1
        if self.real_time_update:
            self.write_end()

    def write_end(self):
        # Write lines to CSV file
        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in self.data:
                writer.writerow(line)
        #print("write complete")

    def make_new_keyframe(self):
        #print("new keyframe added")
        keyframe = [0]*len(self.data[0]) 
        keyframe[0] = self.current_write_frame
        keyframe[1] = self.default_start_node_idx
        return (keyframe)


if __name__ == "__main__":
    keyframe = CSVKeyframe("/media/ducktop/shared/code/cpp/Jointgraph/resources/keyframe.csv")
    keyframe_writer = CSVKeyframe("/media/ducktop/shared/code/cpp/Jointgraph/resources/keyframe.csv")
    keyframe_writer.real_time_update = True

    print(keyframe.data[0][1])

    print(keyframe_writer.data)
    for i in range(0, 40):
        keyframe_writer.write(455+i,address=3)
    print(keyframe_writer.data)
    keyframe_writer.write_end()
