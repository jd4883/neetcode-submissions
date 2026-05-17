class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for x in range(m):
            for y in range(n):
                if target == matrix[x][y]: return True
            #return True
        return False