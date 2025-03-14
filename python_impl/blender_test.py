#decoupling blender impl from testing blender file
import bpy
from bpy.app.handlers import persistent
import sys 
sys.path.insert(0,"/home/duckpcc/dev/code/Jointgraph/python_impl")
sys.path.insert(0,"/home/duckpcc/dev/code/Jointgraph/resources")

from joint_blender_impl import BlenderAngleImpl

test_blender_angle = BlenderAngleImpl("Bone")
hardcode= 0

#https://docs.blender.org/api/current/bpy.app.handlers.html
#TODO: add support for event trigering udp animations


@persistent
def frame_pre_handler_udp_write(dummy):
    print("Load Handler:", test_blender_angle.gather())

@persistent
def frame_pre_handler_udp_listen(dummy):
    hardcode += 1
    test_blender_angle.populate(hardcode)




if __name__ == "__main__":
    print("start")
    bpy.app.handlers.frame_change_pre.append(frame_pre_handler_udp_listen)
