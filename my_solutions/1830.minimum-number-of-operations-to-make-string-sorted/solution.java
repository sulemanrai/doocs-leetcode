class Solution {
    private static final int N = 3010;
    private static final int MOD = (int) 1e9 + 7;
    private static final long[] f = new long[N];
    private static final long[] g = new long[N];

    static {
        f[0] = 1;
        g[0] = 1;
        for (int i = 1; i < N; ++i) {
            f[i] = f[i - 1] * i % MOD;
            g[i] = qmi(f[i], MOD - 2);
        }
    }

    public static long qmi(long a, int k) {
        // TODO: implement
    }
}
