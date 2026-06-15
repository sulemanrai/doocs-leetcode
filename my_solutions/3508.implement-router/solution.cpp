#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <array>
using namespace std;

class Router {
private:
    int lim;
    unordered_set<long long> vis;
    deque<array<int, 3>> q;
    unordered_map<int, int> idx;
    unordered_map<int, vector<int>> d;

    long long f(int a, int b, int c) {
        // TODO: implement
    }
};
