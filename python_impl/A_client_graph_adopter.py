import client
from adj_list import Graph

#TODO:remove in file
import yamlLoader as yl

#acting as an adopter class between udp client and graph/urdf reader
class AClientGraphAdopter(client.Client):
    def __init__(self,
                 client_port= 8888,
                 graph = Graph()):
        super().__init__(client_port)
        #self.graph = make_urdf_graph(config_file)
        self.graph = graph
    
    def get_max_joint_stream(self):
        return self.graph.node_count

    def listen_for_joints(self):
        #place in super class's listen loop like puppet.listen_loop(puppet.listen_for_joints) after subscribing to controller
        int_array = self.get_listen_data()
        if len(int_array) > 0:
            node_start_idx = int_array[0]
            joint_data = int_array[1:-1]
            self.graph.use_bfs(self.graph.set_node_angle,node_start_idx,joint_data)
            #TODO:remove after verifiying
            self.check_joint_states()

    def check_joint_states(self):
        self.graph.use_bfs(self.graph.print_node_angle,0,[])


#no unit test here because this implemtation will be built in the client factory

