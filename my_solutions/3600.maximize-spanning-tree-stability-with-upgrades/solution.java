class UnionFind {
    int[] p, size;
    int cnt;

    UnionFind(int n) {
        p = new int[n];
        size = new int[n];
        cnt = n;
        for (int i = 0; i < n; i++) {
            p[i] = i;
            size[i] = 1;
        }
    }

    int find(int x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }

    boolean union(int a, int b) {
        int pa = find(a), pb = find(b);
        if (pa == pb) return false;
        if (size[pa] > size[pb]) {
            p[pb] = pa;
            size[pa] += size[pb];
        } else {
            p[pa] = pb;
            size[pb] += size[pa];
        }
        cnt--;
        return true;
    }
}

class Solution {

    int n;
    int[][] edges;
    int k;

    private boolean check(int lim) {
        UnionFind uf = new UnionFind(n);

        for (int[] e : edges) {
            int u = e[0], v = e[1], s = e[2];
            if (s >= lim) {
                uf.union(u, v);
            }
        }

        int rem = k;
        for (int[] e : edges) {
            int u = e[0], v = e[1], s = e[2];
            if (s * 2 >= lim && rem > 0) {
                if (uf.union(u, v)) {
                    rem--;
                }
            }
        }

        return uf.cnt == 1;
    }

    public int maxStability(int n, int[][] edges, int k) {
        // TODO: implement
    }
}
