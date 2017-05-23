#ifndef NODE_H
#define NODE_H

#include <string>

class Node
{   
    public:
        Node();
        ~Node();
        Node(int val);
        Node(std::string str);
        Node(int val, std::string str);
        
        void setVal(int val);
        int getVal();
        
        void setStr(std::string str);
        std::string getStr();
        
        Node* getLeftChild();
        void setLeftChild(Node* n);
        Node* getRightChild();
        void setRightChild(Node* n);
        
    private:
        std::string m_str;
        int m_val;
        Node* m_leftchild;
        Node* m_rightchild;
};

#endif
