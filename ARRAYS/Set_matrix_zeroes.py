class Solution:
    def Set_Matrix_Zeroes(self, matrix):
        zero_matrix=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zero_matrix.append((i,j))
        
        for i,j in zero_matrix:
            for col in range(len(matrix[0])):
                 matrix[i][col]=0
            for row in range(len(matrix)):
                matrix[row][j]=0
        return matrix
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
obj = Solution()
print(obj.Set_Matrix_Zeroes(matrix))


'''[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]'''