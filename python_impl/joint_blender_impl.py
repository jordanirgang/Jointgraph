import bpy
import math
from mathutils import Euler
from A_joint_impl import AJointImpl


class BlenderAngleImpl(AJointImpl):

	def __init__ (self, bone_name,bone_armature="Armature",stream_axis='X'):
		self.pose_bone = bpy.data.objects[bone_armature].pose.bones[bone_name]
		self.pose_bone.rotation_mode = 'XYZ'
		self.stream_axis = stream_axis
		self.frame = 0
		self.data_path = ""
		self.axis_dict ={'X':0,'Y':1,'Z':2}
		self.is_animate = False
		self.data_path = "rotation_euler"
		self.joint_angle_axis = [0,0,0]
		self.joint_angle_axis[self.axis_dict[self.stream_axis]] = 1
		print(self.joint_angle_axis)

	def gather(self):
		print(self.axis_dict)
		return self.pose_bone.rotation_euler[self.axis_dict[self.stream_axis]]

	def populate(self,joint_angle):
		self.joint_angle_axis[self.axis_dict[self.stream_axis]] = joint_angle
		print(("tup",self.joint_angle_axis))
		self.pose_bone.rotation_euler= Euler(self.joint_angle_axis,'XYZ')#.rotate_axis(self.stream_axis, math.radians(joint_angle))
		print(self.pose_bone)
		if self.is_animate:
			self.pose_bone.keyframe_insert(data_path=self.data_path, frame=self.frame)	
			self.frame +=1
			#nothing






