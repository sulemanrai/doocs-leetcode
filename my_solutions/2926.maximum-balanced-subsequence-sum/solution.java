class BinaryIndexedTree {
    private int n;
    private long[] c;
    private final long inf = 1L << 60;

    public BinaryIndexedTree(int n) {
        this.n = n;
        c = new long[n + 1];
        Arrays.fill(c, -inf);
    }

    public void update(int x, long v) {
        // TODO: implement
    }
}
