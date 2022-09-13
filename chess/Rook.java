package chess;

public class Rook extends ChessPiece {
    public Rook(String color) {
        super(color);
    }

    @Override
    public String getColor() {
        return color;
    }

    boolean isCorrectFigureMove(int line, int column, int toLine, int toColumn) {
        return (!(line==toLine && column == toColumn)
                && (line == toLine || column == toColumn)
                );
    }

    @Override
    public String getSymbol() {
        return "R";
    }
}
