#include <unordered_map>
using namespace std;

class LRUCache {
private:
    struct Node {
        int key, val;
        Node* prev;
        Node* next;
        Node(int key, int val)
            : key(key)
            , val(val)
            , prev(nullptr)
            , next(nullptr) {
                // TODO: implement
            }
};
