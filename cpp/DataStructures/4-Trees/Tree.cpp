#include "Tree.h"

#include <random>
#include <iostream>

Tree::~Tree()
{   
    delete this->m_head;
}

Tree::Tree(Node* head)
{
    this->m_head = head;
}

Node* Tree::getHead()
{
    return m_head;
}

// Print m_val for each of the nodes in the tree.
//      n is the root node to start printing from.
//      order is an int value representing the order to print in:
//          0 -> inorder
//          1 -> postorder
//          2 -> preorder
void Tree::printVals(Node* n, int order)
{   
    if (n == nullptr)
    {
        return;
    }
    
    if (order == 0)
    {
        // Inorder
        printVals(n->getLeftChild(), order);
        std::cout<<n->getVal()<<"\n";
        printVals(n->getRightChild(), order);
    }
    else if (order == 1)
    {
        // Postorder
        printVals(n->getLeftChild(), order);
        printVals(n->getRightChild(), order);
        std::cout<<n->getVal()<<"\n";
    }
    else if (order == 2)
    {
        // Preorder
        std::cout<<n->getVal()<<"\n";
        printVals(n->getLeftChild(), order);
        printVals(n->getRightChild(), order);
    }
}

// Adds new node to tree randomly.
// Recursively finds an empty node to add new node.
// Should be overwritten in tree implementations that require some sort of balancing/order.
//      head -> current node being looked at.
//      n    -> node being added to tree.
void Tree::addNode(Node* head, Node* n)
{   
    if (this->m_head == nullptr)
    {
        std::cout<<"Added to head\n";
        this->m_head = n;
    }
    else
    {
        if (head->getLeftChild() == nullptr)
        {
            std::cout<<"Added to left\n";
            head->setLeftChild(n);
        }
        else if (head->getRightChild() == nullptr)
        {
            std::cout<<"Added to right\n";
            head->setRightChild(n);
        }
        else
        {
            //Dumb insertion: randomly choose left or right.
            std::random_device gen;
            std::bernoulli_distribution dist(0.5);
            if (dist(gen))
            {
                std::cout<<"going left  ";
                this->addNode(head->getLeftChild(),n);
            }
            else
            {
                std::cout<<"going right  ";
                this->addNode(head->getRightChild(),n);
            }
        }
    }
}
