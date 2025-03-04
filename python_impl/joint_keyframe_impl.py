from A_joint_impl import AJointImpl
from keyframe import CSVKeyframe

class KeyframeAngleImpl(AJointImpl):
    
    def __init__(self,address = 2, start_frame=0, keyframe=CSVKeyframe()):
        self.address = address
        self.frame = start_frame
        self.keyframe_db = keyframe

    def gather(self):
        self.frame+=1
        return self.keyframe_db.read(self.frame-1,self.address)

    def populate(self,joint_angle):
        self.keyframe_db.write(joint_angle,self.address)

#TODO:kind of a factory pattern but lazier, should probably move to a creator
def create_csv_keyframe(path):
    return CSVKeyframe(path)

if __name__ == "__main__":
    keyframe = create_csv_keyframe("/media/ducktop/shared/code/cpp/Jointgraph/resources/keyframe.csv")
    
    test_idx_2 = KeyframeAngleImpl(2,0,keyframe)
    test_idx_3 = KeyframeAngleImpl(3,0,keyframe)

    for i in range(0,3):
        print(("idx_0",test_idx_2.gather()))
        print(("idx_1",test_idx_3.gather()))

