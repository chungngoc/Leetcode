class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # ### Bottom-Up DP
        # triangle = [[1]]

        # for i in range(1, numRows):
        #     prev_row = triangle[-1]
        #     row = [1]

        #     for j in range(1, i):
        #         row.append(prev_row[j-1] + prev_row[j])

        #     row.append(1)
        #     triangle.append(row)

        # return triangle
        
        ### Top-down DP (recursive)
        if numRows == 1:
            return [[1]]

        # Get previous pascal_triangle
        pascal_triangle = self.generate(numRows-1)
        
        # Get current row
        nth_row=[1]
        for i in range(1, len(pascal_triangle[-1])):
            nth_row.append(pascal_triangle[-1][i-1]+pascal_triangle[-1][i])
        nth_row.append(1)
        
        # Generate current triangle
        pascal_triangle.append(nth_row)
        return pascal_triangle
        
        