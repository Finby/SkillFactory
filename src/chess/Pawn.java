package chess;

public class Pawn extends ChessPiece {
    public Pawn(String color) {
        super(color);
    }

    @Override
    public String getColor() {
        return color;
    }

    boolean isCorrectFigureMove(ChessBoard chessBoard, int line, int column, int toLine, int toColumn) {
        if (column != toColumn) {
            if ((this.getColor().equals(WHITE) && chessBoard.board[toLine][toColumn].getColor().equals(BLACK)
                    || this.getColor().equals(BLACK) && chessBoard.board[toLine][toColumn].getColor().equals(WHITE))
                    && Math.abs(column - toColumn) == 1 && Math.abs(line - toLine) == 1
            ) {
                return true;
            }
            return false;
        }
        if (this.getColor().equals(WHITE)) {
            if (line == 1 && (toLine == 2 || toLine == 3)) {
                return true;
            }
            else if (line > 2 && toLine == line + 1){
                return true;
            }
            else {
                return false;
            }
        }
        else {
            if (line == 6 && (toLine == 5 || toLine == 4)) {
                return true;
            }
            else if (line < 6 && toLine == line - 1) {
                return true;
            }
            else {
                return false;
            }
        }
    }

    @Override
    public String getSymbol() {
        return "P";
    }

//    boolean checkPos(int n) {
//        return (MIN_BORDER <= n && n <= MAX_BORDER);
//    }
}
