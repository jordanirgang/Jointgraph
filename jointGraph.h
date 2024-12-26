#pragma once
#include <vector>

using namespace std;
struct Data{
	float address;
	float angle;
};
struct Node{
	vector<Node *> adjacency_list;
	Data* data;


};
class JointGraph{
	public:
		JointGraph();
		void addNode(Node link);
		void addEdge(Node srcLink,Node destLink);

	private:
		vector<Node> nodes;
};


