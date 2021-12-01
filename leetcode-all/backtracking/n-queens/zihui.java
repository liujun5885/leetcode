class Solution {
    
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> answer = new ArrayList<List<String>>();
        int[] queens = new int[n];
        Arrays.fill(queens, -1);
        Set<Integer> left_diagonals = new HashSet<Integer>();
        Set<Integer> right_diagonals = new HashSet<Integer>();
        Set<Integer> columns = new HashSet<Integer>();
        backtrack(answer, queens, n, 0, left_diagonals, right_diagonals, columns);
        return answer;
    }

    public List<String> generateBoard(int[] queens, int n) {
        List<String> board = new ArrayList<String>();
        for (int i = 0; i < n; i++) {
            char[] row = new char[n];
            Arrays.fill(row, '.');
            row[queens[i]] = 'Q';
            board.add(new String(row));
        }
        return board;
    }

    public void backtrack(List<List<String>> answer, int[] queens, int n, int row, Set<Integer> left_diagonals, Set<Integer> right_diagonals, Set<Integer> columns) {
        if (row == n) {
            List<String> board = generateBoard(queens, n);
            answer.add(board);
        } else {
            for (int i = 0; i < n; i++) {
                if (columns.contains(i)) {
                    continue;
                }
                int left_diagonal = row + i;
                int right_diagonal = row - i;
                if (left_diagonals.contains(left_diagonal) | right_diagonals.contains(right_diagonal)) {
                    continue;
                }
                queens[row] = i;
                columns.add(i);
                left_diagonals.add(left_diagonal);
                right_diagonals.add(right_diagonal);
                backtrack(answer, queens, n, row + 1, left_diagonals, right_diagonals, columns);
                queens[row] = -1;
                left_diagonals.remove(left_diagonal);
                right_diagonals.remove(right_diagonal);
                columns.remove(i);
            }
        }
    }
}
