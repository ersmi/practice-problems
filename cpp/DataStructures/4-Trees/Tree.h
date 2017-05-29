#ifndef TREE_H
#define TREE_H

#include "Node.h"
#include <string>

class Tree
{
    public:
        Tree(Node* head);
        ~Tree();
        Node* getHead();
        void printVals(Node* n, int order);
        
        virtual void addNode(Node* head, Node* n);
    
    protected:
        Node* m_head;
};

#endif
