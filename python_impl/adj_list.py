import queue
import sys
from A_data_source import ADataSrc


class Node:
    def __init__(self,data:ADataSrc):
        self.data = data
        self.children = []
        self.is_visit = False
        
    def get_name(self):
        return self.data.get_name()
    
    def get_angle(self):
        return self.data.get_angle()
    
    def set_angle(self,angle):
        return self.data.set_angle(angle)

class Graph:
    def __init__(self):
        self.adj_list = []
        self.look_up = {}
        self.node_count = 0

    def addNode(self,data:ADataSrc):
        if data not in self.look_up:
            self.adj_list.append(Node(data))
            self.look_up[data.name]= self.node_count
            self.node_count +=1

    def addEdge(self,src:int,dest:int):
        self.adj_list[src].children.append(self.adj_list[dest])

    def addEdgeByName(self,src:str,dest:str):
        print(("list",self.adj_list[0]))
        src_int = self.look_up[src]
        dest_int = self.look_up[dest]
        self.addEdge(src_int,dest_int)

    def printAdjacencyList(self):
        for i in self.adj_list:
            sys.stdout.write(str(i.data)+"->")
            for j in i.children:
                sys.stdout.write(str(j.data)+"&")
            sys.stdout.write("\n")

    def get_node_by_idx(self,idx):
        return self.adj_list[idx]
    
    def set_node_by_idx_visit(self,idx,is_visit):
         self.adj_list[idx].is_visit=is_visit

    def bfs_get_joint_angles_queue(self,start):
        node_queue = queue.Queue()
        return_queue = queue.Queue()

        self.set_node_by_idx_visit(start,True)
        node_queue.put(self.get_node_by_idx(start))
        while not node_queue.empty():
            node_current = node_queue.get()       
            return_queue.put(node_current)
            for node in node_current.children:
                if not node.is_visit:
                    node.is_visit = True
                    node_queue.put(node)
        return return_queue

    def set_node_angle(self,node_current:Node,idx:int,angle_idx_array:list):
        #usage should be attaching to update_with_bfs object
        #set graph from int array stream
        node_current.set_angle(angle_idx_array[idx])

    def print_node_angle(self,node_current:Node,idx=None,angle_idx_array=None):
        #usage should be attaching to update_with_bfs object
        print((node_current.get_name(),node_current.get_angle()))

    def get_node_angle(self,node_current:Node,idx:int,angle_idx_array:list):
        #usage should be attaching to update_with_bfs object
        #set int array from graph
        angle_idx_array[idx] = node_current.get_angle()
    
    def use_bfs(self,func,node_start:int,int_array:list):
        #TODO:in bfs streamer seperate int_array and node_start
        #using the same algorithm as BFS
        node_queue = queue.Queue()
        node_un_visit = queue.Queue()
        int_array_idx = 0

        self.set_node_by_idx_visit(node_start,True)
        node_queue.put(self.get_node_by_idx(node_start))

        while not node_queue.empty():
            #hopefully this acts as a pointer...yes, it is pass by refrence
            node_current = node_queue.get()       

            #update happens here
            func(node_current,int_array_idx,int_array)
            int_array_idx +=1
            node_un_visit.put(node_current)
            for node in node_current.children:
                if not node.is_visit:
                    node.is_visit = True
                    node_queue.put(node)

        #reset visit property in data
        while not node_un_visit.empty():
            node_ref = node_un_visit.get()
            node_ref.is_visit= False
            
        


#imports only needed for concrete testing
from A_joint_impl import NullAngleImpl
from A_data_source import DataSrc
import yamlLoader as yl


if __name__ == "__main__":
    graph= Graph()
    #also testing concrete implementation
    graph.addNode(DataSrc("A",NullAngleImpl()))
    graph.addNode(DataSrc("B"))
    graph.addEdge(0,1)
    graph.addEdgeByName("A","B")
    graph.printAdjacencyList()
    
    #tree = ET.parse('/home/ducktop/code/cpp/Jointgraph/python_impl/robot_test.xml')
    #root = tree.getroot()
    #print(root.findall('./link'))
    #for link in root.findall('./link'):
    #    print(link.attrib['name'])
    #for joint in root.findall('./joint'):
    #    data = (joint.find('parent').attrib['link'],
    #            joint.find('child').attrib['link'],
    #            joint.find('origin').attrib['xyz'])

    #    print(data)


    newGraph= make_urdf_graph(yl.URDF_LOCATION)
    print(newGraph)
    newGraph.printAdjacencyList()
    q = newGraph.bfs_get_joint_angles_queue(0)
    print(q)
    while not q.empty():
        node = q.get()
        node.is_visit = False
        print((node.get_name(),node.is_visit,node.get_angle()))

    sample_data = [10 ,40, 50 ,20] 
    start = 0
    newGraph.use_bfs(newGraph.print_node_angle,start,sample_data)
    newGraph.use_bfs(newGraph.set_node_angle,start,sample_data)
    newGraph.use_bfs(newGraph.print_node_angle,start,sample_data)
    
    get_ray = [0,0,0,0]
    newGraph.use_bfs(newGraph.get_node_angle,start,get_ray)
    print(get_ray)





