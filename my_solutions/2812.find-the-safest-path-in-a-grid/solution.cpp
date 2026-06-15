#include <vector>
#include <queue>
#include <utility>
#include <algorithm>
#include <numeric>
using namespace std;

class UnionFind {
public:
    vector<int> p;
    int n;

    UnionFind(int _n)
        : n(_n)
        , p(_n) {
            // TODO: implement
        }
};
