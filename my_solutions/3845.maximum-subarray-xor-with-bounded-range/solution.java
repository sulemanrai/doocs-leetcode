class Solution {

    // Trie node for storing prefix XOR values in binary form
    class TrieNode {
        TrieNode[] children = new TrieNode[2]; // 0 and 1 branches
        int count = 0; // number of prefix values passing through this node
    }

    TrieNode root = new TrieNode();

    // Insert or remove a prefix XOR value from the trie
    void updateTrie(int value, int delta) {
        TrieNode current = root;
        for (int bit = 14; bit >= 0; bit--) {
            int currentBit = (value >> bit) & 1;
            if (current.children[currentBit] == null) {
                current.children[currentBit] = new TrieNode();
            }
            current = current.children[currentBit];
            current.count += delta;
        }
    }

    // Find maximum XOR of given value with any value currently in the trie
    int getMaxXor(int value) {
        TrieNode current = root;
        int maxXor = 0;

        for (int bit = 14; bit >= 0; bit--) {
            int currentBit = (value >> bit) & 1;
            int oppositeBit = 1 - currentBit;

            if (current.children[oppositeBit] != null && current.children[oppositeBit].count > 0) {
                maxXor |= (1 << bit);
                current = current.children[oppositeBit];
            } else {
                current = current.children[currentBit];
            }
        }

        return maxXor;
    }

    public int maxXor(int[] nums, int limit) {
        // TODO: implement
    }
}
