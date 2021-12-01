class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        all_res = []
        queens_y = []
        queens_x_add_y = []
        queens_x_minus_y = []

        def putIQueens(i):
            for j in range(n):
                if j not in queens_y and i - j not in queens_x_minus_y and i + j not in queens_x_add_y:
                    queens_y.append(j)
                    queens_x_add_y.append(i + j)
                    queens_x_minus_y.append(i - j)
                    if i == n - 1:
                        res = [['.'] * n for k in range(n)]
                        for x, y in enumerate(queens_y):
                            res[x][y] = 'Q'
                            res[x] = ''.join(res[x])
                        all_res.append(res)
                    else:
                        putIQueens(i + 1)
                    queens_y.pop()
                    queens_x_add_y.pop()
                    queens_x_minus_y.pop()

        putIQueens(0)
        return all_res