#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <climits>
using namespace std;

class Hashing {
private:
    vector<long> p, h;
    long mod;

public:
    Hashing(const string& word, long base, long mod)
        : p(word.size() + 1, 1)
        , h(word.size() + 1, 0)
        , mod(mod) {
            // TODO: implement
        }
};
