class UnionFind {
    Map<Long, Long> p = new HashMap<>();
    Map<Long, Integer> size = new HashMap<>();

    long find(long x) {
        if (!p.containsKey(x)) {
            p.put(x, x);
            size.put(x, 1);
        }
        if (p.get(x) != x) {
            p.put(x, find(p.get(x)));
        }
        return p.get(x);
    }

    boolean union(long a, long b) {
        long pa = find(a), pb = find(b);
        if (pa == pb) {
            return false;
        }

        int sa = size.get(pa), sb = size.get(pb);
        if (sa > sb) {
            p.put(pb, pa);
            size.put(pa, sa + sb);
        } else {
            p.put(pa, pb);
            size.put(pb, sa + sb);
        }
        return true;
    }
}

class Solution {
    public int maxActivated(int[][] points) {
        // TODO: implement
    }
}
