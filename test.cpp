#include "jointGraph.h"
#include "BFS.h"
#include <iostream>
using namespace std;
int main (){
	JointGraph testGraph= JointGraph();
	Data d = {5, 0};
	Data p = {4,0};
	testGraph.addNode(d);
	testGraph.addNode(p);
	testGraph.addEdge(d,p);
	std::cout << "GRAPH made";
	queue toPrint = bfsJointGraph(testGraph,0);
	while (!toPrint.empty())
	{
		std::cout << toPrint.front()->data->address << " ";
		toPrint.pop();
	}
	cout << "test\n";
	return 0;
}
