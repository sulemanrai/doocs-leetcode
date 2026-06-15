class MedianFinder {
    private final PriorityQueue<Integer> small = new PriorityQueue<>(Comparator.reverseOrder());
    private final PriorityQueue<Integer> large = new PriorityQueue<>();
    private final Map<Integer, Integer> delayed = new HashMap<>();
    private int smallSize;
    private int largeSize;

    public void addNum(int num) {
        // TODO: implement
    }
}
