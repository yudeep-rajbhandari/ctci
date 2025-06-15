def isValid(board,r,c):
    return 0 <= r < len(board) and 0<= c < len(board[0]) and board[r][c] == 0


def spiralOrder(n):
     mat = [[0] * n for i in range(n)]
     direction = [[-1,0],[0,-1],[1,0],[0,1]]
     r,c = n-1,n-1
     i = (n * n)-1
     j = 0
     
     while(i > 0):
          mat[r][c] = i
          i -=1
          if(not isValid(mat, r + direction[j][0], c + direction[j][1])):
               j = (j + 1) % 4
          r , c = r + direction[j][0], c + direction[j][1]
     
          
     print(mat)

spiralOrder(5)
