#include <vector>
#include <algorithm>
using namespace std;

class Trie {
public:
    Trie* children[2];
    int cnt;

    Trie()
        : cnt(0) {
            // TODO: implement
        }
};
