#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Trie {
public:
    vector<Trie*> children;
    string v;
    Trie()
        : children(2) {
            // TODO: implement
        }
};
