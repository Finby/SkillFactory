package chess;

public class Horse extends ChessPiece {



    public Horse(String color) {
        super(color);
    }

    @Override
    public String getColor() {
        return color;
    }

    boolean isCorrectFigureMove(ChessBoard chessBoard, int line, int column, int toLine, int toColumn) {
        return (Math.abs(line - toLine) == 1 && Math.abs(column - toColumn) == 2
                || Math.abs(line - toLine) == 2 && Math.abs(column - toColumn) == 1);
    }

    @Override
    boolean isNobodyOnLine(ChessBoard chessBoard, int line, int column, int toLine, int toColumn) {
        return (chessBoard.board[toLine][toColumn] == null
                || !this.getColor().equals(chessBoard.board[toLine][toColumn].getColor()));
    }

    @Override
    public String getSymbol() {
        return "H";
    }

//    boolean checkPos(int n) {
//        return (MIN_BORDER <= n && n <= MAX_BORDER);
//    }
}
