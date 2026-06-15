class Graph {
    private int n;
    private int[][] g;
    private final int inf = 1 << 29;

    public Graph(int n, int[][] edges) {
        this.n = n;
        g = new int[n][n];
        for (var f : g) {
            Arrays.fill(f, inf);
        }
        for (int[] e : edges) {
            int f = e[0], t = e[1], c = e[2];
            g[f][t] = c;
        }
    }

    public void addEdge(int[] edge) {
        // TODO: implement
    }
}
