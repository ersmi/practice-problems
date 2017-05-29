#ifndef BINARYTREE_H
#define BINARYTREE_H

#include "../Node.h"
#include "../Tree.h"
#include <string>

class BinaryTree : public Tree
{
    public: 
        BinaryTree(Node* head);
        ~BinaryTree();
        void addNode(Node* head, Node* n);
};

#endif
