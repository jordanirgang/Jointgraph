import bpy
import sys 
sys.path.insert(0,"/home/ducktop/code/cpp/Jointgraph/python_impl")
import math
from A_joint_impl import AJointImpl
#https://docs.blender.org/api/current/bpy.app.handlers.html
#TODO: add support for event trigering udp animations

class BlenderAngleImpl(AJointImpl):

	def __init__ (self, bone_name,bone_armature="Armature",stream_axis='x'):
		self.pose_bone = bpy.data.objects[bone_armature].pose.bones[bone_name]
		self.pose_bone.rotation_mode = 'XYZ'
		self.stream_axis = stream_axis
		self.frame = 0
		self.data_path = ""
		self.axis_dict ={'x':0,'y':0,'z':1}


	def gather(self):
		return math.degrees(self.pose_bone.rotation_euler[self.axis_dict[self.stream_axis]])

	def populate(self,joint_angle):
		self.pose_bone.rotation_euler.rotate_axis(self.axis_dict, math.radians(joint_angle))
		if self.is_animate:
			self.pose_bone.keyframe_insert(self.data_path, frame=self.frame)	
			self.frame +=1


if __name__ == "__main__":
	test_blender_angle = BlenderAngleImpl("Bone")
	print(test_blender_angle.gather())



