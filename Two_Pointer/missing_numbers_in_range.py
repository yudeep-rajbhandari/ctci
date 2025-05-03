def run_tests():
  tests = [
      # Example 1 from the book
      ([6, 9, 12, 15, 18], 9, 13, [10, 11, 13]),
      # Example 2 from the book
      ([], 9, 9, [9]),
      # Example 3 from the book
      ([6, 7, 8, 9], 7, 8, []),
      # Additional test cases
      ([], 1, 5, [1, 2, 3, 4, 5]),
      ([1, 2, 3, 4, 5], 1, 5, []),
      ([1, 3, 5], 1, 5, [2, 4]),
      ([1], 1, 1, []),
      ([2], 1, 3, [1, 3]),
  ]
  for arr, low, high, want in tests:
    got = missing_numbers(arr, low, high)
    assert got == want, f"\nmissing_numbers({arr}, {low}, {high}): got: {
        got}, want: {want}\n"

def missing_numbers(arr, low, high):
    l , r = 0, len(arr)-1
    res = []
    k = low
    boundaryL, boundaryR = 0, 0
    while(l <= r):
        if(arr[l] < low):
            l +=1
        if(arr[r] > high):
            r -=1
        if(arr[l] >= low and arr[r] <= high):
                while(low < arr[l]):
                    res.append(low)
                    low +=1
                if(low == arr[l]):
                     low+=1                
                l+=1
    while(low <= high):
         res.append(low)
         low+=1
    return res

run_tests()
        
          
            
