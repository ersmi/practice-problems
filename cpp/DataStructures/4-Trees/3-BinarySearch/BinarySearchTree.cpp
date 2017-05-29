#include "BinarySearchTree.h"

#include <random>
#include <iostream>

BinarySearchTree::BinarySearchTree() : Tree(nullptr)
{
    //
}

BinarySearchTree::~BinarySearchTree()
{
    this->~Tree();
}

// Navigate to left or right subtrees until an empty node is found.
// Will maintain left/right value properties, but does not make any guarantees
//    that the tree will remain balanced, or complete.
// Time Complexity: O(n)
void BinarySearchTree::addNode(Node* head, Node* n)
{   
    if (this->m_head == nullptr)
    {
        this->m_head = n;
        return;
    }
    if (n->getVal() < head->getVal())
    {
        if (head->getLeftChild() == nullptr)
        {
            head->setLeftChild(n);
        }
        else
        {
            this->addNode(head->getLeftChild(),n);
        }
    }
    else // NOTE: if n == head, we add n to right subtree.
    {
        if (head->getRightChild() == nullptr)
        {
            head->setRightChild(n);
        }
        else
        {
            this->addNode(head->getRightChild(),n);
        }
    }
}

// Return true if value is in tree, false otherwise.
// Go through left or right subtree based on whether or not the value to find i is larger.
// Time Complexity: O(n)
bool BinarySearchTree::contains(int i, Node* head)
{
    if (head == nullptr)
    {
        return false;
    }
    if (i == head->getVal())
    {
        return true;
    }
    if (i > head->getVal())
    {
        this->contains(i, head->getRightChild());
    }
    else
    {
        this->contains(i, head->getLeftChild());
    }
}

// Min and max functions only need to search through one side.
// Left for min, right for max.
// Time Complexity: O(n)
int BinarySearchTree::findMax()
{   
    Node* temp = this->m_head;
    while(temp->getRightChild() != nullptr)
    {
        temp = temp->getRightChild();
    }
    return temp->getVal();
}

int BinarySearchTree::findMin()
{   
    Node* temp = this->m_head;
    while(temp->getLeftChild() != nullptr)
    {
        temp = temp->getLeftChild();
    }
    return temp->getVal();
}
