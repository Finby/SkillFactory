package chess;

public class ChessBoard {
    public ChessPiece[][] board = new ChessPiece[8][8]; // creating a field for game
    String nowPlayer;
    static final String WHITE = "White";
    static final String BLACK = "Black";

    public ChessBoard(String nowPlayer) {
        this.nowPlayer = nowPlayer;
    }

    public String nowPlayerColor() {
        return this.nowPlayer;
    }

    public boolean moveToPosition(int startLine, int startColumn, int endLine, int endColumn) {
        if (checkPos(startLine) && checkPos(startColumn)) {

            if (!nowPlayer.equals(board[startLine][startColumn].getColor())) return false;

            if (board[startLine][startColumn].canMoveToPosition(this, startLine, startColumn, endLine, endColumn)) {

                if (board[startLine][startColumn].getSymbol().equals("K") ||  // check position for castling
                        board[startLine][startColumn].getSymbol().equals("R")) {
                    board[startLine][startColumn].check = false;
                }

                board[endLine][endColumn] = board[startLine][startColumn]; // if piece can move, we moved a piece
                board[startLine][startColumn] = null; // set null to previous cell
                this.nowPlayer = this.nowPlayerColor().equals("White") ? "Black" : "White";

                return true;
            } else return false;
        } else return false;
    }

    public void printBoard() {  //print board in console
        System.out.println("Turn " + nowPlayer);
        System.out.println();
        System.out.println("Player 2(Black)");
        System.out.println();
        System.out.println("\t0\t1\t2\t3\t4\t5\t6\t7");
        for (int i = 7; i > -1; i--) {
            System.out.print(i + "\t");
            for (int j = 0; j < 8; j++) {
                if (board[i][j] == null) {
                    System.out.print(".." + "\t");
                } else {
                    System.out.print(board[i][j].getSymbol() + board[i][j].getColor().substring(0, 1).toLowerCase() + "\t");
                }
            }
            System.out.println();
            System.out.println();
        }
        System.out.println("Player 1(White)");
    }

    public boolean checkPos(int pos) {
        return pos >= 0 && pos <= 7;
    }

    public boolean castling0() {
        int line = (nowPlayer.equals(WHITE)) ? 0 : 7;
        String opponentPlayerColor = (nowPlayer.equals(WHITE)) ? BLACK : WHITE;

        if (board[line][0] == null || board[line][4] == null) return false;
        if (board[line][0].getSymbol().equals("R") && board[line][4].getSymbol().equals("K") && // check that King and Rook
                board[line][1] == null && board[line][2] == null && board[line][3] == null) {              // never moved
            if (board[line][0].getColor().equals(nowPlayer) && board[line][4].getColor().equals(nowPlayer) &&
                    board[line][0].check && board[line][4].check &&
                    !new King(nowPlayer).isUnderAttack(this, line, 2)) { // check that position not in under attack
                board[line][4] = null;
                board[line][2] = new King(nowPlayer);   // move King
                board[line][2].check = false;
                board[line][0] = null;
                board[line][3] = new Rook(nowPlayer);   // move Rook
                board[line][3].check = false;
                nowPlayer = opponentPlayerColor;  // next turn
                return true;
            } else return false;
        } else return false;
    }

    public boolean castling7() {
        int line = (nowPlayer.equals(WHITE)) ? 0 : 7;
        String opponentPlayerColor = (nowPlayer.equals(WHITE)) ? BLACK : WHITE;

        if (board[line][7] == null || board[line][4] == null) return false;
        if (board[line][7].getSymbol().equals("R") && board[line][4].getSymbol().equals("K") && // check that King and Rook
                board[line][5] == null && board[line][6] == null) {              // never moved
            if (board[line][7].getColor().equals(nowPlayer) && board[line][4].getColor().equals(nowPlayer) &&
                    board[line][7].check && board[line][4].check &&
                    !new King(nowPlayer).isUnderAttack(this, line, 6)) { // check that position not in under attack
                board[line][4] = null;
                board[line][6] = new King(nowPlayer);   // move King
                board[line][6].check = false;
                board[line][7] = null;
                board[line][5] = new Rook(nowPlayer);   // move Rook
                board[line][5].check = false;
                nowPlayer = opponentPlayerColor;  // next turn
                return true;
            } else return false;
        } else return false;
    }
}