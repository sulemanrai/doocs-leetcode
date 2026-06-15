class Cashier {
    private int i;
    private int n;
    private int discount;
    private Map<Integer, Integer> d = new HashMap<>();

    public Cashier(int n, int discount, int[] products, int[] prices) {
        this.n = n;
        this.discount = discount;
        for (int j = 0; j < products.length; ++j) {
            d.put(products[j], prices[j]);
        }
    }

    public double getBill(int[] product, int[] amount) {
        // TODO: implement
    }
}
