
class AJointImpl:
    def __init__():
        pass

    def gather(self)->float:
        #virtual method for pulling a joint angle from a location
        return 0
    
    def populate(self,joint_angle:float):
        #virtual method for populating locations with angles
        pass

class NullAngleImpl(AJointImpl):
    
    def __init__(self,hardcoded=0):
        self.hardcoded = hardcoded

    #@overrides(AGatherImpl)
    def gather(self):
        return self.hardcoded

    #@overrides(AGatherImpl)
    def populate(self,joint_angle):
        self.hardcoded = joint_angle
        print(("null setter used, ",joint_angle))