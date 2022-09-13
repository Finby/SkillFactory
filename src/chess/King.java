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
                !isCorrectFigureMove(chessBoard, line, column, toLine, toColumn)
                || !isNobodyOnLine(chessBoard, line, column, toLine, toColumn)
                || isUnderAttack(chessBoard, toLine, toColumn)
        )
        ) {
            return false;
        }
        return true;
    }

    boolean isCorrectFigureMove(ChessBoard chessBoard, int line, int column, int toLine, int toColumn) {
        return (!(line==toLine && column == toColumn)
                && Math.abs(line - toLine) <= 1 && Math.abs(column - toColumn) <= 1
        );
    }

    public boolean isUnderAttack(ChessBoard chessBoard, int toLine, int toColumn) {
        String opponentColor = (this.getColor().equals(WHITE)) ? BLACK : WHITE;
        for (int i = MIN_BORDER; i < MAX_BORDER; i++) {
            for (int j = MIN_BORDER; j < MAX_BORDER; j++) {
                // figure and it can go to position [line][column]
                if (chessBoard.board[i][j] != null && chessBoard.board[i][j].getColor().equals(opponentColor)
                        && chessBoard.board[i][j].canMoveToPosition(chessBoard, i, j, toLine, toColumn)) {
                    return true;
                }
            }
        }
        return false;
    }


    private Boolean cellIsAttacked(int line, int column, String opponentColor) {
        return false;
    }


}
