#include <vector>
#include <string>
using namespace std;

class BinaryIndexedTree {
public:
    int n;
    vector<int> c;

    BinaryIndexedTree(int n)
        : n(n)
        , c(n + 1, 0) {
            // TODO: implement
        }
};
