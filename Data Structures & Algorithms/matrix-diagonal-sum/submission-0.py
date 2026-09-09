class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total_sum = 0    
        for i in range(n):
            total_sum += mat[i][i]
            total_sum += mat[i][n-i-1]

        if n % 2 == 1:
            center = n // 2
            total_sum -= mat[center][center]
        return total_sum
