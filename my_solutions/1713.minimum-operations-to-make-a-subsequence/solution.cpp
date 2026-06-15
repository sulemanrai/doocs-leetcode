#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class BinaryIndexedTree {
private:
    int n;
    vector<int> c;

public:
    BinaryIndexedTree(int n)
        : n(n)
        , c(n + 1) {
            // TODO: implement
        }
};
