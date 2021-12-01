class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int):
            if row == n:
                board = generate_board()
                ans.append(board)
            else:
                for i in range(n):
                    if i in columns or row + i in left_diagonals or row - i in right_diagonals:
                        # cannot place Q here
                        continue
                    queens[row] = i
                    columns.add(i)
                    left_diagonals.add(row + i)
                    right_diagonals.add(row - i)
                    backtrack(row + 1)
                    columns.remove(i)
                    left_diagonals.remove(row + i)
                    right_diagonals.remove(row - i)

        
        def generate_board():
            board = []
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.' # revert change for row
            return board

        columns, left_diagonals, right_diagonals = set(), set(), set() # left_diagonals = row + col, right_diagonals = row - col
        row = ['.'] * n
        queens = [-1] * n
        ans = []
        backtrack(0)
        return ans
