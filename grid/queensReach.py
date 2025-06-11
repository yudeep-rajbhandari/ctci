def run_tests():
  tests = [
      ([[0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0]],
       [[1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1]]),
      # Edge case - empty board
      ([], []),
      # Edge case - 1x1 board with queen
      ([[1]], [[1]]),
      # Edge case - 1x1 board without queen
      ([[0]], [[0]]),
      # Edge case - no queens
      ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
  ]

  for board, want in tests:
    got = safe_cells(board)
    assert got == want, f"\nsafe_cells({board}): got: {got}, want: {want}\n"

def isValid(board,r,c):
    return 0 <= r < len(board) and 0<= c < len(board[0]) and board[r][c] != 1



def findStuff(r,c,valid_direction,res):
    for x,y in valid_direction:
        a,b = x+r, y+c
        while(isValid(res,a,b)):
            res[a][b] = 1
            a = a + x
            b = b + y



def safe_cells(board):
    rlen = len(board)
    res = [[0] * rlen for _ in range(rlen)]
    valid_direction = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
 
    j = 0
    for i in range(rlen):
        for j in range(rlen):
            if(board[i][j] == 1):
                res[i][j] = 1
                findStuff(i,j,valid_direction,res)
    
    return res

run_tests()