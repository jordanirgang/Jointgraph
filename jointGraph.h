#pragma once
#include <vector>

using namespace std;
struct Data{
	float address;
	float angle;
};
struct Node{
	vector<Node *> adjacencyList;
	Data* data;
};

class JointGraph{
	public:
		JointGraph();
		~JointGraph();
		void addNode(Data linkData);
		void addEdge(Node srcLink,Node destLink);

	private:
		int nodeCount;
		vector<Node> nodes;
};


