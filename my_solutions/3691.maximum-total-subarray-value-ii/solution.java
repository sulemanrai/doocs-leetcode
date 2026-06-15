class SparseTableRMQ {
    int n;
    int maxLog;
    int[][] fMax;
    int[][] fMin;
    int[] lg;

    public SparseTableRMQ(int[] data) {
        this.n = data.length;
        this.maxLog = 32 - Integer.numberOfLeadingZeros(n) + 1;
        this.fMax = new int[n][maxLog];
        this.fMin = new int[n][maxLog];
        this.lg = new int[n + 1];

        for (int i = 2; i <= n; i++) {
            this.lg[i] = this.lg[i >> 1] + 1;
        }

        for (int i = 0; i < n; i++) {
            this.fMax[i][0] = data[i];
            this.fMin[i][0] = data[i];
        }

        for (int j = 1; j < maxLog; j++) {
            for (int i = 0; i <= n - (1 << j); i++) {
                this.fMax[i][j]
                    = Math.max(this.fMax[i][j - 1], this.fMax[i + (1 << (j - 1))][j - 1]);
                this.fMin[i][j]
                    = Math.min(this.fMin[i][j - 1], this.fMin[i + (1 << (j - 1))][j - 1]);
            }
        }
    }

    public int queryMax(int l, int r) {
        // TODO: implement
    }
}
