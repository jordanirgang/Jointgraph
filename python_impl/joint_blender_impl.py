import sys 
sys.path("/")
import bpy
import math
from A_joint_impl import AJointImpl

class BlenderAngleImpl(AjointImpl)
	axis_dict ={'X':0,'Y':0,'Z':1}

	def __init__ (self, bone_name,bone_armature="Armature",stream_axis='X'):
		self.pose_bone = bpy.data.objects(bone_armature).pose.bones[bone_name]
		self.pose_bone.rotation_mode='XYZ'
		self.stream_axis = stream_axis
		self.frame = 0

	def gather(self):
		return self.pose_bone.euler_rotation[axis_dict[self.stream_axis]]

	def populate(self,joint_angle)
		self.pose_bone.rotation_euler.rotate_axis(axis, math.radians(joint_angle))
		if self.is_animate:
			self.pose_bone.keyframe_insert(data_path, frame=self.frame)	
			self.frame +=1



