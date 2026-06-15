class BinaryIndexedTree {
    int n;
    int[] c;

    BinaryIndexedTree(int n) {
        this.n = n;
        this.c = new int[n + 1];
    }

    void update(int x, int delta) {
        while (x <= n) {
            c[x] += delta;
            x += x & -x;
        }
    }

    int query(int x) {
        int s = 0;
        while (x > 0) {
            s += c[x];
            x -= x & -x;
        }
        return s;
    }
}

class Solution {
    public int[] minDeletions(String s, int[][] queries) {
        // TODO: implement
    }
}
