package chess;

public class King extends ChessPiece {
    public King(String color) {
        super(color);
    }

    @Override
    public String getSymbol() {
        return "K";
    }

    @Override
    public String getColor() {
        return color;
    }

    @Override
    public boolean canMoveToPosition(ChessBoard chessBoard, int line, int column, int toLine, int toColumn) {
        if ((!checkPos(line) || !checkPos(column) || !checkPos(toLine) || !checkPos(toColumn) ||
                !isCorrectFigureMove(line, column, toLine, toColumn)
                || !isNobodyOnLine(chessBoard, line, column, toLine, toColumn)
                || isUnderAttack(chessBoard, toLine, toColumn)
        )
        ) {
            return false;
        }
        return true;
    }

    boolean isCorrectFigureMove(int line, int column, int toLine, int toColumn) {
        return (!(line==toLine && column == toColumn)
                && Math.abs(line - toLine) <= 1 && Math.abs(column - toColumn) <= 1
        );
    }

    boolean isUnderAttack(ChessBoard board, int line, int column) {
        String opponentColor = (getColor().equals(WHITE)) ? BLACK : WHITE;
        Boolean isAttacked = cellIsAttacked(line, column, opponentColor);


        return false;
    }

    private Boolean cellIsAttacked(int line, int column, String opponentColor) {
        return false;
    }
}
