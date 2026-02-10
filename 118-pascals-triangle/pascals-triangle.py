class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
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
        
        