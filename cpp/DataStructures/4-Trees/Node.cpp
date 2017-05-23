#include "Node.h"

Node::Node()
{   
    this->m_str = "";
    this->m_val = -1;
    this->m_leftchild = nullptr;
    this->m_rightchild = nullptr;
}

Node::~Node()
{
    if (this->m_leftchild != nullptr)
        delete m_leftchild;
    if (this->m_rightchild != nullptr)
        delete m_rightchild;
}

Node::Node(int val)
{   
    this->m_str = "";
    this->m_val = val;
    this->m_leftchild = nullptr;
    this->m_rightchild = nullptr;
}

Node::Node(std::string str)
{   
    this->m_str = str;
    this->m_val = -1;
    this->m_leftchild = nullptr;
    this->m_rightchild = nullptr;
}

Node::Node(int val, std::string str)
{   
    this->m_str = str;
    this->m_val = val;
    this->m_leftchild = nullptr;
    this->m_rightchild = nullptr;
}

void Node::setVal(int val)
{   
    this->m_val = val;
}

int Node::getVal()
{   
    return m_val;
}

void Node::setStr(std::string str)
{
    this->m_str = str;
}

std::string Node::getStr()
{
    return m_str;
}

Node* Node::getLeftChild()
{
    return m_leftchild;
}

void Node::setLeftChild(Node* n)
{
    this->m_leftchild = n;
}

Node* Node::getRightChild()
{
    return m_rightchild;
}

void Node::setRightChild(Node* n)
{
    this->m_rightchild = n;
}
