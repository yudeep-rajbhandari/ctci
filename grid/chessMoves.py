def run_tests():
  tests = [
      # Example 1 from the book - king moves
      ([[0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]], "king", 3, 5,
          [[2, 5], [3, 4], [4, 4], [4, 5]]),
      # Example 2 from the book - knight moves
      ([[0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]], "knight", 4, 3,
       [[2, 2], [3, 5], [5, 5]]),
      # Example 3 from the book - queen moves
      ([[0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]], "queen", 4, 4,
       [[3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5],
        [5, 3], [5, 4], [5, 5]]),
      # Edge case - 1x1 board
      ([[0]], "queen", 0, 0, []),
      # Edge case - all occupied except current position
      ([[1, 1], [1, 0]], "knight", 1, 1, []),
  ]

  for board, piece, r, c, want in tests:
    got = chess_moves(board, piece, r, c)
    # Sort both lists for consistent comparison
    got.sort()
    want.sort()
    assert got == want, (f"\nchess_moves({board}, {piece}, {r}, {c}): "
                         f"got: {got}, want: {want}\n")


def isValid(board,r,c):
    return 0 <= r < len(board) and 0<= c < len(board[0]) and board[r][c] != 1

def chess_moves(board, piece, r, c):
    result = []
    if(piece == 'king'):
        valid_direction = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        for x,y in valid_direction:
            a, b = r+x , c+y
            if(isValid(board, a,b)):
                result.append([a,b])

    elif(piece == 'knight'):
        valid_direction=[[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
        for x,y in valid_direction:
            a, b = r+x , c+y
            if(isValid(board, a,b)):
                result.append([a,b])
    else:
        valid_direction= [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        j = 1
        removal = []
        while(len(valid_direction) > 0):
            for x, y in valid_direction:
                a, b = x * j, y *j
                a,b = r+a, c+b
                if(isValid(board,a,b)):
                    result.append([a,b])
                else:
                    removal.append([x,y])
            for x, y in valid_direction:
                if([x,y] in removal):
                    valid_direction.remove([x,y])
            j +=1
    return result


run_tests()

    

