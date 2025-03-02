from A_joint_impl import AJointImpl
from keyframe import Keyframe

class KeyframeAngleImpl(AJointImpl):
    
    def __init__(self,address, frame=0):
        self.address = address
        self.frame = frame
        #keyframe read- frame index , value_location
        self.joint_angle = Keyframe.read(frame,address) 

    def gather(self):
        pass

    def populate(self,):
        pass

