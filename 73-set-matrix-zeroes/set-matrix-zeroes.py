class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = set()
        n = len(matrix[0])
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for j in range(n):
                    if matrix[i][j] == 0:
                        col.add(j)
                matrix[i] = [0] * n
        for k in list(col):
            for arr in matrix:
                arr[k] = 0

        return matrix
        