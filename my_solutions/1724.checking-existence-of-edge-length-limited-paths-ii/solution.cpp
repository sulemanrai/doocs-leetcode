#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class PersistentUnionFind {
private:
    vector<int> rank;
    vector<int> parent;
    vector<int> version;

public:
    PersistentUnionFind(int n)
        : rank(n, 0)
        , parent(n)
        , version(n, INT_MAX) {
            // TODO: implement
        }
};
