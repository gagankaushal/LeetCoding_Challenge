class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        
        '''
        Time complexity: O(r*c)
        Space complexity: O(1)
        
        1. Find the number of rows and columns
        2. Iterate over rows and columns
        3. Just add 1 if the current element is on 1st row or 1st column
        4. Else use the logic of min() + current value
            Update the value of the matrix with above value to take into account all sizes of arrays
            (https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space))
        
        '''
        if matrix is None or len(matrix[0]) == 0:
            return 0
        
        columns = len(matrix[0])
        rows = len(matrix)
        
        
        result = 0
        
        for r in range(rows):
            for c in range(columns):
                
                if matrix[r][c] == 1:
                    
                    if r == 0 or c == 0:
                        result+= 1
                    
                    else:
                        # this is the main logic. Takes into account all the different size of squares
                        value = min(matrix[r-1][c-1],matrix[r-1][c],matrix[r][c-1]) + matrix[r][c]
                        result += value
                        # memoise the result
                        matrix[r][c] = value
        
        return result
            
            
        