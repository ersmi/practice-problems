#include "BinaryTree.h"

#include <random>
#include <iostream>

BinaryTree::BinaryTree(Node* head) : Tree(head)
{
    //
}

BinaryTree::~BinaryTree()
{
    this->~Tree();
}

void BinaryTree::addNode(Node* head, Node* n)
{   
    // Use the random addition implementation.
    Tree::addNode(head,n);
}
