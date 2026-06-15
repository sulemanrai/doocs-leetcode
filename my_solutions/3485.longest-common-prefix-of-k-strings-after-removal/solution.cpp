#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    struct TrieNode {
        int count = 0;
        int depth = 0;
        int children[26] = {0};
    };

    class SegmentTree {
    public:
        int n;
        vector<int> tree;
        vector<int>& globalCount;
        SegmentTree(int n, vector<int>& globalCount)

            : n(n)

            , globalCount(globalCount) {
                // TODO: implement
            }
};
