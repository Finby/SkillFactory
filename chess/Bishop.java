package chess;

public class Bishop extends ChessPiece {
    public Bishop(String color) {
        super(color);
    }

    @Override
    public String getColor() {
        return color;
    }


    boolean isCorrectFigureMove(int line, int column, int toLine, int toColumn) {
        return (Math.abs(line - toLine) == Math.abs(column - toColumn)
                && !(line==toLine && column == toColumn));
    }

    @Override
    public String getSymbol() {
        return "B";
    }
}
