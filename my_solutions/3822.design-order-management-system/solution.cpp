#include <vector>
#include <string>
#include <unordered_map>
#include <utility>
using namespace std;

class OrderManagementSystem {
    using Key = pair<string, int>;

    struct KeyHash {
        size_t operator()(const Key& k) const {
            return hash<string>()(k.first) ^ (hash<int>()(k.second) << 1);
        }
    };

    unordered_map<int, string> orderTypeMap;
    unordered_map<int, int> priceMap;
    unordered_map<Key, vector<int>, KeyHash> t;

public:
    OrderManagementSystem() {
        // TODO: implement
    }
};
