class Solution {
    private TreeSet<int[]> l = new TreeSet<>((a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
    private TreeSet<int[]> r = new TreeSet<>(l.comparator());
    private Map<Integer, Integer> cnt = new HashMap<>();
    private long s;

    public long[] findXSum(int[] nums, int k, int x) {
        // TODO: implement
    }
}
