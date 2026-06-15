#include <unordered_map>
#include <set>
#include <utility>
using namespace std;

class AuctionSystem {
    unordered_map<int, set<pair<int, int>>> items;
    unordered_map<int, unordered_map<int, int>> users;

public:
    AuctionSystem() {
        // TODO: implement
    }
};
