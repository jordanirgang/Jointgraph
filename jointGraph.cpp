#include <vector>
#include "jointGraph.h"

using namespace std;
JointGraph::JointGraph(){
//init graph
	this->nodes = vector<Node>();
	this->nodeCount= 0;
}
JointGraph::~JointGraph(){

}

void JointGraph::addNode(Data linkData){
	Node nodeToAdd;
	nodeToAdd.data = &linkData;
	nodeToAdd.adjacencyList= vector<Node *>();
	this->nodes.push_back(nodeToAdd);
	this->nodeCount ++;

}

void JointGraph::addEdge(Node srcLink, Node destLink){
	srcLink.adjacencyList.push_back(&destLink);
}



