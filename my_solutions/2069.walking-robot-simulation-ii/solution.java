class Robot {

    private int mx, my, p, cur;
    private boolean moved;

    public Robot(int width, int height) {
        this.mx = width - 1;
        this.my = height - 1;
        this.p = 2 * this.mx + 2 * this.my;
        this.cur = 0;
        this.moved = false;
    }

    public void step(int num) {
        // TODO: implement
    }
}
