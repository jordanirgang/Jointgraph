import client
from adj_list import Graph,make_urdf_graph

#TODO:remove in file
import yamlLoader as yl

#acting as an adopter class between udp client and graph/urdf reader
class Puppet(client.Client):
    def __init__(self,server_ip="127.0.0.1",server_port=8080,client_port= 8888,config_file="robot_urdf.xml"):
        super().__init__(server_ip,server_port,client_port)
        self.graph = make_urdf_graph(config_file)
    
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

    
if __name__ == "__main__":
    puppet = Puppet(client_port=yl.dictionary['client']['port'],config_file = yl.dictionary['urdf']['location'])
    puppet.subscribe(server_ip= yl.dictionary['server']['ip'], server_port = yl.dictionary['server']['port'])
    puppet.no_timeout()
    puppet.listen_loop(puppet.listen_for_joints)

