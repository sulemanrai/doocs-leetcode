class EventManager {
    private TreeSet<int[]> sl;
    private Map<Integer, Integer> d;

    public EventManager(int[][] events) {
        sl = new TreeSet<>((a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });
        d = new HashMap<>();
        for (int[] e : events) {
            int eventId = e[0], priority = e[1];
            sl.add(new int[] {-priority, eventId});
            d.put(eventId, priority);
        }
    }

    public void updatePriority(int eventId, int newPriority) {
        // TODO: implement
    }
}
