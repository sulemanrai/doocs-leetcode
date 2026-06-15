#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Trie {
public:
    unordered_map<string, Trie*> children;
    bool deleted = false;
};

class Solution {
public:
    vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& paths) {
        // TODO: implement
    }
};
