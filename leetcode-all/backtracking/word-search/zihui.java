class Solution {
    public boolean exist(char[][] board, String word) {
        int rows = board.length, cols = board[0].length;
        boolean[][] visited = new boolean[rows][cols];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                boolean output = check(board, word, visited, r, c, 0);
                if (output) {
                    return true;
                }
            }
        }
        return false;
    }
    private boolean check(char[][] board, String word, boolean[][] visited, int r, int c, int k) {
        if (board[r][c] != word.charAt(k))
            return false;
        if (k == word.length() - 1)
            return true;
        
        int rows = board.length, cols = board[0].length;
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        visited[r][c] = true;
        boolean res = false;

        for (int[] d: directions) {
            int rd = r + d[0], rc = c + d[1];
            if (0 <= rd && rd < rows && 0 <= rc && rc < cols && visited[rd][rc] == false) {
                boolean output = check(board, word, visited, rd, rc, k + 1);
                if (output) {
                    res = true;
                    break;
                }
                
            }
        }
        visited[r][c] = false;
        return res;
    }
}
