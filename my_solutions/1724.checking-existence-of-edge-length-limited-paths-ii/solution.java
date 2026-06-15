class PersistentUnionFind {
    private final int inf = 1 << 30;
    private int[] rank;
    private int[] parent;
    private int[] version;

    public PersistentUnionFind(int n) {
        rank = new int[n];
        parent = new int[n];
        version = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            version[i] = inf;
        }
    }

    public int find(int x, int t) {
        // TODO: implement
    }
}
