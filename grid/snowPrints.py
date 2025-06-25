def run_tests():
  tests = [
      # Example from book
      ([[0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1]], 1),
      # Edge case - top of grid
      ([[1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]], 0),
      # Edge case - bottom of grid
      ([[0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1]], 2),
      # Edge case - single column
      ([[0], [1], [0]], 1),
      # Edge case - single row
      ([[1]], 0),
      # Edge case - zigzag path
      ([[0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 1]], 1),
      # Test max up/down movement
      ([[0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]], 1),
      # Test staying at same level
      ([[0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]], 1),
      # Test going up then down
      ([[0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1]], 1)
  ]

  for field, want in tests:
    got = distance_to_river(field)
    assert got == want, f"\ndistance_to_river({field}): got: {
        got}, want: {want}\n"

def distance_to_river(board):
    R,C = len(board), len(board[0])
    r,c =0,0
    directions= [[-1,1],[0,1],[1,1]]
    min = 9999999
    while(board[r][c] != 1):
        r+=1
    min = r

    new_r, new_c = 0, 0
    while(new_c < C):
        for dir in directions:
            new_r , new_c = r+dir[0], c+dir[1]
            if(0<=new_r < R and 
               0 <= new_c < C and
                 board[new_r][new_c] ==1):
                r , c = new_r, new_c
                
                break
        min = r if r <=min else min
    return min

run_tests()


        
