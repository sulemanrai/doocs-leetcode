class Node {
    int key, val;
    Node prev, next;

    Node() {
    }

    Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    private int size;
    private int capacity;
    private Node head = new Node();
    private Node tail = new Node();
    private Map<Integer, Node> cache = new HashMap<>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        // TODO: implement
    }
}
