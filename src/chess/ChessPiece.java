package chess;

public abstract class ChessPiece {
    String color;
    boolean check;
    static final int MIN_BORDER = 0;
    static final int MAX_BORDER = 7;
    static final String WHITE = "White";
    static final String BLACK = "Black";

    public ChessPiece(String color) {
        this.color = color;
        this.check = true;
    }

    public abstract String getColor();

    public boolean canMoveToPosition(ChessBoard chessBoard, int line, int column, int toLine, int toColumn) {
        if ((!checkPos(line) || !checkPos(column) || !checkPos(toLine) || !checkPos(toColumn)
                || !isCorrectFigureMove(chessBoard, line, column, toLine, toColumn)
                || !isNobodyOnLine(chessBoard, line, column, toLine, toColumn)
                    && isNotYourFigure(chessBoard, toLine, toColumn)
        )
        ) {
            return false;
        }
        return true;
    }

    private boolean isNotYourFigure(ChessBoard chessBoard, int toLine, int toColumn) {
        return !(chessBoard.board[toLine][toColumn] != null
                && this.getColor().equals(chessBoard.board[toLine][toColumn].getColor()));
    }

    abstract boolean isCorrectFigureMove(ChessBoard chessBoard, int line, int column, int toLine, int toColumn);

    public abstract String getSymbol();
    boolean checkPos(int n) {
        return (MIN_BORDER <= n && n <= MAX_BORDER);
    }

    boolean isNobodyOnLine(ChessBoard chessBoard, int line, int column, int toLine, int toColumn) {
        int[] t = getDirectionXY(line, column, toLine, toColumn);
        int dLine = t[0];
        int dColumn = t[1];

        int currentLine = line + dLine;
        int currentColumn = column + dColumn;

        while (!(currentLine == toLine && currentColumn == toColumn) ) {
            if (chessBoard.board[currentLine][currentColumn] != null) {
                return false;
            }
            currentLine += dLine;
            currentColumn += dColumn;
        }
        // check if last position is occupied in canMaveMethod
//        if (chessBoard.board[currentLine][currentColumn] != null
//                && this.getColor().equals(chessBoard.board[currentLine][currentColumn].getColor())) {
//            return false;
//        }
        return true;
    }

    int[] getDirectionXY(int line, int column, int toLine, int toColumn) {
        int dLine, dColumn;
        if (line < toLine) {
            dLine = 1;
        } else if (line == toLine ) {
            dLine = 0;
        }
        else {
            dLine = -1;
        }
        if (column < toColumn) {
            dColumn = 1;
        } else if (column == toColumn ) {
            dColumn = 0;
        }
        else {
            dColumn = -1;
        }
        return new int[] {dLine, dColumn};
    }



}
