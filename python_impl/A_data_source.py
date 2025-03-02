from A_joint_impl import AJointImpl

class NullAngleImpl(AJointImpl):
    
    def __init__(self,hardcoded=0):
        self.hardcoded = hardcoded

    #@overrides(AGatherImpl)
    def gather(self):
        return self.hardcoded

    #@overrides(AGatherImpl)
    def populate(self,joint_angle):
        print(("null setter used, ",joint_angle))

class ADataSrc:
    #the angle insinuated here is at the end of the link
    angle=0

    def __init__(self,xml_data:str, impl=NullAngleImpl()):
        self.name=str(xml_data)
        self.impl = impl

    def get_name(self):
        return self.name

    def set_angle(self, angle):
        self.impl.populate(angle)

    def get_angle(self):
        return self.impl.gather()

