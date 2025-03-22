#decoupling blender impl from testing blender file
import bpy
from bpy.app.handlers import persistent
import sys 
sys.path.insert(0,"/home/ducktop/code/cpp/Jointgraph/python_impl")
sys.path.insert(0,"/home/ducktop/code/cpp/Jointgraph/resources")

from joint_blender_impl import BlenderAngleImpl

is_view_animation = False


test_blender_angle = BlenderAngleImpl("Bone")
test_blender_angle.is_animate = True
hardcode= 0

#https://docs.blender.org/api/current/bpy.app.handlers.html


@persistent
def frame_pre_handler_udp_write(dummy):
    print("Load Handler:", test_blender_angle.gather())

@persistent
def frame_pre_handler_udp_listen(dummy):
    hardcode = 1
    test_blender_angle.populate(hardcode)
    
def unregister_all_handlers():
    while(len(bpy.app.handlers.frame_change_pre) >0):
        bpy.app.handlers.frame_change_pre.pop(0)
    

if __name__ == "__main__":
    #print("start")
    if not is_view_animation:
        unregister_all_handlers()
        bpy.app.handlers.frame_change_pre.append(frame_pre_handler_udp_listen)
        print(len(bpy.app.handlers.frame_change_pre))
    else:
        unregister_all_handlers()
