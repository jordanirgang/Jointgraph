from server import Server
from adj_list import Graph

#TODO:remove in file
import yamlLoader as yl

#acting as an adopter class between udp client and graph/urdf reader
class AServerGraphAdopter(Server):
    def __init__(self,
                 server_ip= "",
                 server_port=8080,
                 graph = Graph()):
        super().__init__(server_ip,server_port)
        #self.graph = make_urdf_graph(config_file)
        self.graph = graph
    
    def get_max_joint_stream(self):
        return self.graph.node_count

    def publish_joints(self, node_start_idx=0):
        #read graphi and publish

        #only add start index, byte stream handler(hidden) takes care of adding the frame 
        joint_data = [node_start_idx]
        self.graph.use_bfs(self.graph.get_node_angle,node_start_idx,joint_data)
        print (joint_data)
        #TODO:add stream part as
        self.publish_int_array(joint_data)

    def check_joint_states(self):
        self.graph.use_bfs(self.graph.print_node_angle,0,[])


#no unit test here because this implemtation will be built in the client factory

