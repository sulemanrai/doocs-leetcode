class RideSharingSystem {
    private int t;
    private TreeSet<int[]> riders;
    private TreeSet<int[]> drivers;
    private Map<Integer, Integer> d;

    public RideSharingSystem() {
        this.t = 0;
        this.riders = new TreeSet<>(
            (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        this.drivers = new TreeSet<>(
            (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        this.d = new HashMap<>();
    }

    public void addRider(int riderId) {
        // TODO: implement
    }
}
