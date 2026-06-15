/**
 * This is the interface for the expression tree Node.
 * You should not remove it, and you can define some classes to implement it.
 */

abstract class Node {
    public abstract int evaluate();
    // define your fields here
    protected String val;
    protected Node left;
    protected Node right;
};

class MyNode extends Node {
    public MyNode(String val) {
        this.val = val;
    }

    public int evaluate() {
        // TODO: implement
    }
}
