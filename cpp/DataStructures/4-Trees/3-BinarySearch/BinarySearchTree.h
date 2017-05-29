#ifndef BINARYSEARCHTREE_H
#define BINARYSEARCHTREE_H

#include "../Node.h"
#include "../Tree.h"
#include <string>

class BinarySearchTree : public Tree
{
    public: 
        BinarySearchTree();
        ~BinarySearchTree();
        void addNode(Node* head, Node* n);
        
        // Unique functions to BST:
        bool contains(int i, Node* head);
        int findMax();
        int findMin();
};

#endif
