#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Trie {
public:
    vector<Trie*> children;
    bool isEnd;
    Trie()
        : children(26)
        , isEnd(false) {
            // TODO: implement
        }
};
