#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>
using namespace std;

class Node {
public:
    int l, r, cnt, length;
};

class SegmentTree {
public:
    vector<Node*> tr;
    vector<int> nums;

    SegmentTree(vector<int>& nums) {
        // TODO: implement
    }
};
