#include <vector>
#include <string>
using namespace std;

class Trie {
private:
    const int inf = 1 << 30;
    Trie* children[26];
    int length = inf;
    int idx = inf;

public:
    Trie() {
        // TODO: implement
    }
};
