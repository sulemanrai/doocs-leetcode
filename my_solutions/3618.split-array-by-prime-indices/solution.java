class Solution {
    private static final int M = 100000 + 10;
    private static boolean[] primes = new boolean[M];

    static {
        for (int i = 0; i < M; i++) {
            primes[i] = true;
        }
        primes[0] = primes[1] = false;

        for (int i = 2; i < M; i++) {
            if (primes[i]) {
                for (int j = i + i; j < M; j += i) {
                    primes[j] = false;
                }
            }
        }
    }

    public long splitArray(int[] nums) {
        // TODO: implement
    }
}
