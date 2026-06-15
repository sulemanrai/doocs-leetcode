#include <vector>
#include <unordered_map>
#include <set>
#include <utility>
using namespace std;

class RideSharingSystem {
private:
    int t;
    set<pair<int, int>> riders;
    set<pair<int, int>> drivers;
    unordered_map<int, int> d;

public:
    RideSharingSystem() {
        // TODO: implement
    }
};
