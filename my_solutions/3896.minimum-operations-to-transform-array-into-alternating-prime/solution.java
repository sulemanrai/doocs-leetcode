class Solution {
    private static final int MX = 200000;
    private static final boolean[] IS_PRIME = new boolean[MX + 1];
    private static final List<Integer> PRIMES = new ArrayList<>();

    static {
        Arrays.fill(IS_PRIME, true);
        IS_PRIME[0] = false;
        IS_PRIME[1] = false;
        for (int i = 2; i <= MX / i; ++i) {
            if (IS_PRIME[i]) {
                for (int j = i * i; j <= MX; j += i) {
                    IS_PRIME[j] = false;
                }
            }
        }
        for (int i = 2; i <= MX; ++i) {
            if (IS_PRIME[i]) {
                PRIMES.add(i);
            }
        }
    }

    public int minOperations(int[] nums) {
        // TODO: implement
    }
}
