class Encrypter {
    private Map<Character, String> mp = new HashMap<>();
    private Map<String, Integer> cnt = new HashMap<>();

    public Encrypter(char[] keys, String[] values, String[] dictionary) {
        for (int i = 0; i < keys.length; ++i) {
            mp.put(keys[i], values[i]);
        }
        for (String w : dictionary) {
            cnt.merge(encrypt(w), 1, Integer::sum);
        }
    }

    public String encrypt(String word1) {
        // TODO: implement
    }
}
