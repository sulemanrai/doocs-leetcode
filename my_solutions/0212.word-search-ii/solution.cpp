#include <vector>
#include <string>
using namespace std;

class Trie {
public:
    vector<Trie*> children;
    int ref;

    Trie()
        : children(26, nullptr)
        , ref(-1) {
            // TODO: implement
        }
};
