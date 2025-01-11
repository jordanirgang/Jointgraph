import sys
import xml.etree.ElementTree as ET
class Data:
	jointAngle=0
	def __init__(self,xml_data:tuple):
		self.name=str(xml_data[0])+"->"+str(xml_data[1])
	def setAngle(self, angle):
		self.angle = angle
	def getAngle(self):
		return self.angle

class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

class Graph:
    def __init__(self):
        self.adj_list = []
        self.look_up = {}
        self.node_count = 0

    def addNode(self,data):
        if data not in self.look_up:
            self.adj_list.append(Node(data))
            self.look_up[data]= self.node_count
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

    def bfsGetJointAnglesQueue(self,start):
        node_queue = []
        return_queue = []

def urdf2graph(path:str):
    graph=Graph()
    tree = ET.parse(path)
    root = tree.getroot()
    for link in root.findall('./link'):
        graph.addNode(link.attrib['name'])
    for joint in root.findall('./joint'):
        data = (joint.find('parent').attrib['link'],
                joint.find('child').attrib['link'],
                joint.find('origin').attrib['xyz'])
        graph.addEdgeByName(data[0],data[1])
    return graph
    


if __name__ == "__main__":
    graph= Graph()
    graph.addNode("A")
    graph.addNode("B")
    graph.addEdge(0,1)
    graph.addEdgeByName("A","B")
    graph.printAdjacencyList()
    tree = ET.parse('robot_test.xml')
    root = tree.getroot()
    print(root.findall('./link'))
    for link in root.findall('./link'):
        print(link.attrib['name'])
    for joint in root.findall('./joint'):
        data = (joint.find('parent').attrib['link'],
                joint.find('child').attrib['link'],
                joint.find('origin').attrib['xyz'])
        print(data)
    newGraph= urdf2graph('robot_test.xml')
    print(newGraph)
    newGraph.printAdjacencyList()


