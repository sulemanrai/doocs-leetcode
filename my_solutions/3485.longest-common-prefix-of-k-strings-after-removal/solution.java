class Solution {
    static class TrieNode {
        int count = 0;
        int depth = 0;
        int[] children = new int[26];

        TrieNode() {
            for (int i = 0; i < 26; ++i) children[i] = -1;
        }
    }

    static class SegmentTree {
        int n;
        int[] tree;
        int[] globalCount;

        SegmentTree(int n, int[] globalCount) {
            this.n = n;
            this.globalCount = globalCount;
            this.tree = new int[4 * (n + 1)];
            for (int i = 0; i < tree.length; i++) tree[i] = -1;
            build(1, 1, n);
        }

        void build(int idx, int l, int r) {
            if (l == r) {
                tree[idx] = globalCount[l] > 0 ? l : -1;
                return;
            }
            int mid = (l + r) / 2;
            build(idx * 2, l, mid);
            build(idx * 2 + 1, mid + 1, r);
            tree[idx] = Math.max(tree[idx * 2], tree[idx * 2 + 1]);
        }

        void update(int idx, int l, int r, int pos, int newVal) {
            if (l == r) {
                tree[idx] = newVal > 0 ? l : -1;
                return;
            }
            int mid = (l + r) / 2;
            if (pos <= mid) {
                update(idx * 2, l, mid, pos, newVal);
            } else {
                update(idx * 2 + 1, mid + 1, r, pos, newVal);
            }
            tree[idx] = Math.max(tree[idx * 2], tree[idx * 2 + 1]);
        }

        int query() {
            return tree[1];
        }
    }

    public int[] longestCommonPrefix(String[] words, int k) {
        // TODO: implement
    }
}
