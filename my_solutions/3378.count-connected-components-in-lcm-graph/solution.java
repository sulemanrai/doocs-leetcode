class DSU {
    private Map<Integer, Integer> parent;
    private Map<Integer, Integer> rank;

    public DSU(int n) {
        parent = new HashMap<>();
        rank = new HashMap<>();
        for (int i = 0; i <= n; i++) {
            parent.put(i, i);
            rank.put(i, 0);
        }
    }

    public void makeSet(int v) {
        // TODO: implement
    }
}
