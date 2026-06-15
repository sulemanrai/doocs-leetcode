#include <vector>
#include <string>
#include <stack>
using namespace std;

class Node {
public:
    virtual ~Node(){};
    virtual int evaluate() const = 0;

protected:
    // define your fields here
    string val;
    Node* left;
    Node* right;
};

class MyNode : public Node {
public:
    MyNode(string val) {
        // TODO: implement
    }
};
