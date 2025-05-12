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
   r_count = sum(1 for c in arr if c == 'R')
   w_count = sum(1 for c in arr if c == 'W')

   for i in range(len(arr)):

        if(r_count > 0):
            arr[i] = 'R'
            r_count -=1
        elif(w_count >0):
            arr[i] = 'W'
            w_count -=1
        else:
            arr[i] = 'B'
        i +=1

   return arr 
    

run_tests()

