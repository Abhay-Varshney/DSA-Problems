class Solution:
    def Rotate_Matrix(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        Rotated_matrix=[[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                Rotated_matrix[j][n-i-1]=matrix[i][j]
        return Rotated_matrix
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
obj = Solution()
print(obj.Rotate_Matrix(matrix))

'''[[1, 3, 0], [3, 4, 1], [1, 5, 2], [5, 2, 0]]'''