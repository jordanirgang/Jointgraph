from A_joint_impl import AJointImpl,NullAngleImpl

#define interface
class ADataSrc:
   def get_name(self):
       pass
   def set_angle(self):
       pass
   def get_angle(self):
       pass
   

#Generic data source 
class DataSrc(ADataSrc):
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

