class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        temp = {i: [] for i in range(-(n-1), m)}
        for i in range(m):
            for j in range(n):
                temp[i-j].append(mat[i][j])
        for v in temp.values():
            v.sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = temp[i-j].pop()
        return mat
