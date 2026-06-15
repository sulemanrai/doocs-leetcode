class Solution {
    private static final List<Integer> p = new ArrayList<>();

    static {
        int N = 1 << 14;
        for (int i = 0; i < N; i++) {
            String s = Integer.toBinaryString(i);
            String rs = new StringBuilder(s).reverse().toString();
            if (s.equals(rs)) {
                p.add(i);
            }
        }
    }

    public int[] minOperations(int[] nums) {
        // TODO: implement
    }
}
