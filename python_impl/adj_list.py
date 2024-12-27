import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

class Graph:
    def __init__(self):
        self.adj_list = []
    def addNode(self,data):
        self.adj_list.append(Node(data))

    def addEdge(self,src:int,dest:int):
        self.adj_list[src].children.append(self.adj_list[dest])
    def printAdjacencyList(self):
        for i in self.adj_list:
            sys.stdout.write(i.data)
            for j in i.children:
                sys.stdout.write("->" + str(j.data)+"\n")
            sys.stdout.write("\n")



if __name__ == "__main__":
    graph= Graph()
    graph.addNode("A")
    graph.addNode("B")
    graph.addEdge(0,1)
    graph.printAdjacencyList()
