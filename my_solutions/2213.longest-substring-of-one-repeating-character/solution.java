class Node {
    int l, r;
    int lmx, rmx, mx;

    Node(int l, int r) {
        this.l = l;
        this.r = r;
        lmx = rmx = mx = 1;
    }
}

class SegmentTree {
    private char[] s;
    private Node[] tr;

    public SegmentTree(char[] s) {
        int n = s.length;
        this.s = s;
        tr = new Node[n << 2];
        build(1, 1, n);
    }

    public void build(int u, int l, int r) {
        // TODO: implement
    }
}
