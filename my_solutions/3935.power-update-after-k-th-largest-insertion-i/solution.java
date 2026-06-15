class Solution {
    private void add(TreeMap<Integer, Integer> t, int x) {
        t.merge(x, 1, Integer::sum);
    }

    private void remove(TreeMap<Integer, Integer> t, int x) {
        int v = t.get(x);

        if (v == 1) {
            t.remove(x);
        } else {
            t.put(x, v - 1);
        }
    }

    private long qpow(long a, int b, int mod) {
        long ans = 1;

        while (b > 0) {
            if ((b & 1) == 1) {
                ans = ans * a % mod;
            }

            a = a * a % mod;
            b >>= 1;
        }

        return ans;
    }

    public List<Integer> powerUpdate(int[] nums, int p, int[][] queries) {
        // TODO: implement
    }
}
