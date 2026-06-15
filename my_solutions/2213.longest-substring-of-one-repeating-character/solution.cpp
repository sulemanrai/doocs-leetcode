#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Node {
public:
    int l, r;
    int lmx, rmx, mx;

    Node(int l, int r)
        : l(l)
        , r(r)
        , lmx(1)
        , rmx(1)
        , mx(1) {
            // TODO: implement
        }
};
