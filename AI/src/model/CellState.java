package model;

import javafx.scene.shape.Rectangle;

public class CellState extends Rectangle {

    private int puzzNumber;
    private double size;

    public CellState(int num, double size) {
        puzzNumber = num;
        this.size = size;
        this.setWidth(size);
        this.setHeight(size);
    }

    @Override
    public int hashCode() {
        return super.hashCode() + puzzNumber;
    }
}
