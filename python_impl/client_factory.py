from A_client_graph_adopter import AClientGraphAdopter
from joint_keyframe_impl import KeyframeAngleImpl,create_csv_keyframe
from A_joint_impl import NullAngleImpl
from A_data_source import DataSrc
from adj_list import Graph
import xml.etree.ElementTree as ET


class Client_Factory:
    def create_csv_keyframe_instance(xml_path:str,
                CSV_path:str,
                client_port= 8888):
        #TODO: implement strategy pattern for this algorithm but for swithching impl
        graph=Graph()
        tree = ET.parse(xml_path)
        root = tree.getroot()

        #TODO: diffrence here is the IMPL added to the DataSrc Obect 
        csv_db = create_csv_keyframe(CSV_path)

        list_address = 0
        for link in root.findall('./link'):
            #TODO: diffrence here is the IMPL added to the DataSrc Obect 
            graph.addNode(DataSrc(link.attrib['name'],
                                  KeyframeAngleImpl(list_address,0,csv_db)))

        for joint in root.findall('./joint'):
            data = (joint.find('parent').attrib['link'],
                    joint.find('child').attrib['link'],
                    joint.find('origin').attrib['xyz'])
            
            graph.addEdgeByName(data[0],data[1])

        client_to_build = AClientGraphAdopter(client_port,graph)
        return client_to_build
    
    def create_print_out_instance(xml_path:str, client_port= 8888):
        graph=Graph()
        tree = ET.parse(xml_path)
        root = tree.getroot()

        list_address = 0
        for link in root.findall('./link'):
            graph.addNode(DataSrc(link.attrib['name'],
                                  NullAngleImpl(list_address)))

        for joint in root.findall('./joint'):
            data = (joint.find('parent').attrib['link'],
                    joint.find('child').attrib['link'],
                    joint.find('origin').attrib['xyz'])
            
            graph.addEdgeByName(data[0],data[1])

        client_to_build = AClientGraphAdopter(client_port,graph)
        return client_to_build
        


import yamlLoader as yl
import os
if __name__ == "__main__":
    cwd = os.getcwd()
    csv_file = os.path.join(str(cwd),"resources/network_config.yaml")    
    #puppet = Client_Factory.create_csv_keyframe_instance(xml_path=yl.URDF_LOCATION,CSV_path=csv_file,client_port=yl.dictionary['client']['port'])
    puppet = Client_Factory.create_print_out_instance(xml_path=yl.URDF_LOCATION,client_port=yl.dictionary['client']['port'])

    puppet.subscribe(server_ip= yl.dictionary['server']['ip'], server_port = yl.dictionary['server']['port'])
    puppet.no_timeout()
    puppet.listen_loop(puppet.listen_for_joints)