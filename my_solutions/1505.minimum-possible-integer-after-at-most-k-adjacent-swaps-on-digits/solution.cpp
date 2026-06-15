#include <vector>
#include <string>
#include <queue>
using namespace std;

class BinaryIndexedTree {
public:
    int n;
    vector<int> c;

    BinaryIndexedTree(int _n)
        : n(_n)
        , c(_n + 1) {
            // TODO: implement
        }
};
