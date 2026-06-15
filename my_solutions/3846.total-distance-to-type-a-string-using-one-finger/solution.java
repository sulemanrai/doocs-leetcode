class Solution {
    private static final Map<Character, int[]> pos = new HashMap<>();

    static {
        String[] keys = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        for (int i = 0; i < keys.length; i++) {
            for (int j = 0; j < keys[i].length(); j++) {
                pos.put(keys[i].charAt(j), new int[] {i, j});
            }
        }
    }

    public int totalDistance(String s) {
        // TODO: implement
    }
}
