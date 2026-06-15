#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Node {
public:
    int l = 0, r = 0;
    int mn = 0, mx = 0;
    int lazy = 0;
};

/*
 * Segment Tree that supports:
 *  1. Range add
 *  2. Query the smallest index whose prefix sum equals a given value
 */
class SegmentTree {
public:
    SegmentTree(int n) {
        // TODO: implement
    }
};
