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
    p1 = 0
    p2 = low
    res = []
    while(p1 < len(arr) and p2 <=high):
        if(arr[p1] < p2):
            p1 +=1
        elif(arr[p1] == p2):
            p1+=1
            p2+=1
        else:
            res.append(p2)
            p2 +=1
    
    while(p2 <=high):
       res.append(p2)
       p2 +=1
    return res
    
     

run_tests()
        
          
            
