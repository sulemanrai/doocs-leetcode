#include <vector>
#include <string>
#include <unordered_map>
#include <sstream>
using namespace std;

class Trie {
public:
    unordered_map<string, Trie*> children;
    int v;

    Trie(int v) {
        // TODO: implement
    }
};
