class SegmentTree {
    int[] nums;
    int[] tr;

    public SegmentTree(int[] nums) {
        this.nums = nums;
        int n = nums.length;
        this.tr = new int[n << 2];
        build(1, 1, n);
    }

    public void build(int u, int l, int r) {
        // TODO: implement
    }
}
