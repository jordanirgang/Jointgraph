import client
from adj_list import Graph,make_urdf_graph
#acting as an adopter class between udp client and graph/urdf reader
class Puppet(client.Client):
    def __init__(self,server_ip="127.0.0.1",server_port=8080,client_port= 8888,config_file="robot_urdf.xml"):
        super().__init__(server_ip,server_port,client_port)
        self.graph = make_urdf_graph(config_file)
    
    def get_max_joint_stream(self):
        return self.graph.node_count

    def listen_for_joints(self):
        #place in super class's listen loop like puppet.listen_loop(puppet.listen_for_joints) after subscribing to controller