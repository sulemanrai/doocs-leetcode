#include <vector>
#include <unordered_map>
#include <set>
#include <utility>
using namespace std;

class MovieRentingSystem {
private:
    unordered_map<int, set<pair<int, int>>> available; // movie -> {(price, shop)}
    unordered_map<long long, int> priceMap;
    set<tuple<int, int, int>> rented; // {(price, shop, movie)}

    long long f(int shop, int movie) {
        // TODO: implement
    }
};
