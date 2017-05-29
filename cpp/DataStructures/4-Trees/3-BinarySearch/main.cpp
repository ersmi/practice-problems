#include "../Node.cpp"
#include "../Tree.cpp"
#include "BinarySearchTree.cpp"

#include <string>
#include <iostream>

int TESTCASE[10] = { 4, 6, 1, 5, 3, 9, 0, 2, 8, 7 };

int main(int argc, char** argv)
{   
    std::cout<<"Adding 0-10 to BST...\n";
    BinarySearchTree* b = new BinarySearchTree();
    for (int i=0; i<10; i++)
    {
        Node* newNode = new Node(TESTCASE[i]);
        b->addNode(b->getHead(), newNode);
    }
    
    std::cout<<"Inorder:\n";
    b->printVals(b->getHead(),0);
    std::cout<<"Postorder:\n";
    b->printVals(b->getHead(),1);
    std::cout<<"Preorder:\n";
    b->printVals(b->getHead(),2);
    
    std::cout<<"Contains(5)\n";
    std::cout<<b->contains(5,b->getHead())<<"\n";
    std::cout<<"Contains(15)\n";
    std::cout<<b->contains(15,b->getHead())<<"\n";
    
    std::cout<<"FindMax()\n";
    std::cout<<b->findMax()<<"\n";
    std::cout<<"FindMin()\n";
    std::cout<<b->findMin()<<"\n";
}
