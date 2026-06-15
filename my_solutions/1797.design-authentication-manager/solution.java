class AuthenticationManager {
    private int t;
    private Map<String, Integer> d = new HashMap<>();

    public AuthenticationManager(int timeToLive) {
        t = timeToLive;
    }

    public void generate(String tokenId, int currentTime) {
        // TODO: implement
    }
}
