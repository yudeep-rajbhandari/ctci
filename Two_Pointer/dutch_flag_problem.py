def run_tests():
  tests = [
      # Example from the book
      (list("RWBBWRW"), list("RRWWWBB")),
      # Additional test cases
      ([], []),
      (list("R"), list("R")),
      (list("W"), list("W")),
      (list("B"), list("B")),
      (list("RW"), list("RW")),
      (list("WR"), list("RW")),
      (list("RWB"), list("RWB")),
      (list("RRRWWBBB"), list("RRRWWBBB")),
      (list("BBBWWRRR"), list("RRRWWBBB")),
  ]
  for arr, want in tests:
    arr_copy = arr.copy()  # Make a copy since function modifies in place
    sort_colors(arr_copy)
    assert arr_copy == want, f"\nsort_colors({arr}): got: {
        arr_copy}, want: {want}\n"

def sort_colors(arr):
    l , r = 0, len(arr)-1
    while(l < r):
        if(arr[l] == 'R' or arr[l] == 'W'):
            l +=1
        elif(arr[r] == 'B'):
            r -=1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l +=1
            r -=1
    boundary = 0
    for i in range(len(arr)):
       if(arr[i] == 'R' or arr[i] == 'W'):
          boundary +=1
    l , r = 0, boundary-1
    while(l < r):
        if(arr[l] == 'R'):
            l +=1
        elif(arr[r] == 'W'):
            r -=1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l +=1
            r -=1
    return arr
    

run_tests()

