class Trie {
    Trie[] children = new Trie[26];

    void insert(String w) {
        Trie node = this;
        for (int i = 0; i < w.length(); ++i) {
            int j = w.charAt(i) - 'a';
            if (node.children[j] == null) {
                node.children[j] = new Trie();
            }
            node = node.children[j];
        }
    }
}

class Solution {
    private Integer[] f;
    private char[] s;
    private Trie trie;
    private final int inf = 1 << 30;

    public int minValidStrings(String[] words, String target) {
        // TODO: implement
    }
}
