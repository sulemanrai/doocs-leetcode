class Twitter {
    private Map<Integer, List<Integer>> userTweets;
    private Map<Integer, Set<Integer>> userFollowing;
    private Map<Integer, Integer> tweets;
    private int time;

    /** Initialize your data structure here. */
    public Twitter() {
        userTweets = new HashMap<>();
        userFollowing = new HashMap<>();
        tweets = new HashMap<>();
        time = 0;
    }

    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        // TODO: implement
    }
}
