#include "../Node.cpp"
#include "../Tree.cpp"
#include "BinaryTree.cpp"

#include <string>
#include <iostream>

int main(int argc, char** argv)
{   
    BinaryTree* b = new BinaryTree(nullptr);
    for (int i=0; i<10; i++)
    {
        Node* newNode = new Node(i);
        b->addNode(b->getHead(), newNode);
    }
    
    std::cout<<"Inorder print of 0-10:\n";
    b->printVals(b->getHead(),0);
    std::cout<<"Postorder print of 0-10:\n";
    b->printVals(b->getHead(),1);
    std::cout<<"Preorder print of 0-10:\n";
    b->printVals(b->getHead(),2);
}
