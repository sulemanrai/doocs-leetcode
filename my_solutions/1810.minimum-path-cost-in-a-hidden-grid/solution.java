/**
 * // This is the GridMaster's API interface.
 * // You should not implement it, or speculate about its implementation
 * class GridMaster {
 *     boolean canMove(char direction);
 *     int move(char direction);
 *     boolean isTarget();
 * }
 */

class Solution {
    private final int m = 200;
    private final int n = 200;
    private final int inf = Integer.MAX_VALUE / 2;
    private final int[] dirs = {-1, 0, 1, 0, -1};
    private final char[] s = {'U', 'R', 'D', 'L'};
    private int[][] g;
    private int sx = 100, sy = 100;
    private int tx = -1, ty = -1;
    private GridMaster master;

    public int findShortestPath(GridMaster master) {
        // TODO: implement
    }
}
