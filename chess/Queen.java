package chess;

public class Queen extends ChessPiece {
    public Queen(String color) {
        super(color);
    }

    @Override
    public String getSymbol() {
        return "Q";
    }

    @Override
    public String getColor() {
        return color;
    }

    boolean isCorrectFigureMove(int line, int column, int toLine, int toColumn) {
        return (!(line==toLine && column == toColumn)
                && ((line == toLine || column == toColumn)
                    || Math.abs(line - toLine) == Math.abs(column - toColumn)
                    )
        );
    }

}
