#include <vector>
#include <algorithm>
using namespace std;

class Node {
public:
    int l, r;
    long long s00, s01, s10, s11;

    Node(int l, int r)
        : l(l)
        , r(r)
        , s00(0)
        , s01(0)
        , s10(0)
        , s11(0) {
            // TODO: implement
        }
};
