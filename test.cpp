#include "jointGraph.h"
#include <iostream>
using namespace std;
int main (){
	JointGraph testGraph= JointGraph();
	Data d = {5, 0};
	Data p = {4,0};
	testGraph.addNode(d);
	testGraph.addNode(p);
	cout << "test\n";
	return 0;
}
