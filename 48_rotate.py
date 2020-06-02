class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # note the i and j range
        for i in range(n//2):
            for j in range(n//2 + n%2):
                r, c = i, j
                s = matrix[n-1-c][r]
                #print(s, n-1-c, r)
                for k in range(4):
                    #matrix[r][c] = matrix[n-1-c][r]
                    t = matrix[r][c]
                    matrix[r][c] = s 
                    s = t
                    #matrix[c][n-1-r] = matrix[r][c]
                    print(r,c)
                    r, c = c, n-1-r
                    print(r,c)
                    print('pair')
                print('four')
        

