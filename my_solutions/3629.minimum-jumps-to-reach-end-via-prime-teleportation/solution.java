class Solution {
    private static final int mx = 1000001;
    private static final List<Integer>[] factors = new List[mx];

    static {
        for (int i = 0; i < mx; i++) {
            factors[i] = new ArrayList<>();
        }
        for (int i = 2; i < mx; i++) {
            if (factors[i].isEmpty()) {
                for (int j = i; j < mx; j += i) {
                    factors[j].add(i);
                }
            }
        }
    }

    public int minJumps(int[] nums) {
        // TODO: implement
    }
}
