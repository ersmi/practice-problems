#ifndef TREE_H
#define TREE_H

#include "../Node.h"
#include <string>

class BinaryTree
{
    public:
        BinaryTree();
        ~BinaryTree();
        BinaryTree(Node* head);
        
        Node* getHead();
    
        void addNode(Node* head, Node* n);
        
        void printVals(Node* n, int order);
    
    private:
        Node* m_head;
};

#endif
