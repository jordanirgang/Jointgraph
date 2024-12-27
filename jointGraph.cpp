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
	if(this->lookUp.find(&linkData) == this->lookUp.end()){
		Node nodeToAdd;
		nodeToAdd.data = &linkData;
		nodeToAdd.adjacencyList= vector<Node *>();
		nodeToAdd.UUID= this->nodeCount;

		this->nodes.push_back(nodeToAdd);
		this->lookUp[this->nodes.back().data] = 0;
		this->nodeCount ++;
	}
		
}

void JointGraph::addEdge(Node srcLink, Node destLink){
	srcLink.adjacencyList.push_back(&destLink);
}

void JointGraph::addEdge(Data srcDataLookup, Data destDataLookup)
{
	if(this->lookUp.find(&srcDataLookup) == this->lookUp.end() && this->lookUp.find(&destDataLookup) == this->lookUp.end() ){
		this->addEdge(this->lookUp.at(&srcDataLookup),this->lookUp.at(&destDataLookup)); 
	}
}

void JointGraph::addEdge(int srcIdx, int destIdx)
{
	this->addEdge(nodes.at(srcIdx),this->nodes.at(destIdx));
}
