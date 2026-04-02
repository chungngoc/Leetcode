class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        new_matrix = []
        if len(matrix) > 1:
            for j in range(len(matrix[0])-1, -1,-1):
                l = []
                for i in range(1, len(matrix)):
                    l.append(matrix[i][j])
                new_matrix.append(l)
            return matrix[0] + self.spiralOrder(new_matrix)
        else:
            return matrix[0]
    