#pragma once
#include <vector>
#include <unordered_map>


using namespace std;
struct Data{
	float address;
	float angle;
};
struct Node{
	vector<Node *> adjacencyList;
	Data* data;
	int UUID;
	bool isVisit;
};

class JointGraph{
	public:
		JointGraph();
		~JointGraph();
		void addNode(Data linkData);
		void addEdge(Node srcLink,Node destLink);
		void addEdge(Data srcDataLookup, Data destDataLookup);
		void addEdge(int srcLink,int destLink);
		Node* getNodeByIdxAdded(int idx);
		vector<Node*> getAdjacentNodes(int nodeIdx);

	private:
		int nodeCount;
		vector<Node> nodes;
		unordered_map<Data*,int> lookUp = unordered_map<Data *,int>();
};


