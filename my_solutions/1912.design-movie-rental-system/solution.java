class MovieRentingSystem {
    private Map<Integer, TreeSet<int[]>> available = new HashMap<>();
    private Map<Long, Integer> priceMap = new HashMap<>();
    private TreeSet<int[]> rented = new TreeSet<>((a, b) -> {
        if (a[0] != b[0]) {
            return a[0] - b[0];
        }
        if (a[1] != b[1]) {
            return a[1] - b[1];
        }
        return a[2] - b[2];
    });

    public MovieRentingSystem(int n, int[][] entries) {
        for (int[] entry : entries) {
            int shop = entry[0], movie = entry[1], price = entry[2];
            available
                .computeIfAbsent(movie, k -> new TreeSet<>((a, b) -> {
                    if (a[0] != b[0]) {
                        return a[0] - b[0];
                    }
                    return a[1] - b[1];
                }))
                .add(new int[] {price, shop});
            priceMap.put(f(shop, movie), price);
        }
    }

    public List<Integer> search(int movie) {
        // TODO: implement
    }
}
