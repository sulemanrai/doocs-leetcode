class Solution {
    private static final int[] f = new int[10];

    static {
        f[0] = 1;
        for (int i = 1; i < 10; i++) {
            f[i] = f[i - 1] * i;
        }
    }

    public boolean isDigitorialPermutation(int n) {
        // TODO: implement
    }
}
