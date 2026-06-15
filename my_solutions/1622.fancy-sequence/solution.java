class Node {
    Node left;
    Node right;
    int l;
    int r;
    int mid;
    long v;
    long add;
    long mul = 1;

    public Node(int l, int r) {
        this.l = l;
        this.r = r;
        this.mid = (l + r) >> 1;
    }
}

class SegmentTree {
    private Node root = new Node(1, (int) 1e5 + 1);
    private static final int MOD = (int) 1e9 + 7;

    public SegmentTree() {
    }

    public void modifyAdd(int l, int r, int inc) {
        // TODO: implement
    }
}
