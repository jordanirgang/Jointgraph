#ifndef BFS_H
#define BFS_H

#include "jointGraph.h"
#include <iostream>
#include <queue>
#include <vector>

using namespace std;
//BFS print
queue<Node*>  bfsJointGraph(JointGraph &jg, int nodeStart){
    queue<Node*> nodeQueue = queue<Node*>();
    queue<Node*> returnQueue = queue<Node*>();
    jg.getNodeByIdxAdded(nodeStart)->isVisit = true;
    //adjacency list never added to
    nodeQueue.push(jg.getNodeByIdxAdded(nodeStart));
    
    Node* current;
    while(!nodeQueue.empty()){
        current = nodeQueue.front();
        nodeQueue.pop();
        returnQueue.push(current);

        for(Node* node: current->adjacencyList){
            if(!node->isVisit){
                node->isVisit = true;
                nodeQueue.push(node);
            }
        }
    }

   // delete current;
    return returnQueue;
}
#endif
