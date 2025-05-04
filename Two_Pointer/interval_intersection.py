def run_tests():
  tests = [
      # Example 1 from the book
      ([[0, 1], [4, 6], [7, 8]], [[2, 3], [5, 9], [10, 11]], [[5, 6], [7, 8]]),
      # Example 2 from the book
      ([[2, 4], [5, 8]], [[3, 3], [4, 7]], [[3, 3], [4, 4], [5, 7]]),
      # Additional test cases
      ([], [], []),
      ([[1, 2]], [], []),
      ([[1, 3]], [[2, 4]], [[2, 3]]),
      ([[1, 5]], [[2, 3]], [[2, 3]]),
      ([[1, 2], [3, 4]], [[2, 3]], [[2, 2], [3, 3]]),
  ]
  for arr1, arr2, want in tests:
    got = interval_intersection(arr1, arr2)
    assert got == want, f"\ninterval_intersection({arr1}, {arr2}): got: {
        got}, want: {want}\n"

def interval_intersection(arr1, arr2):
    p1 , p2 = 0 , 0
    res = []
    while(p1 < len(arr1) and p2 < len(arr2)):
        if(arr1[p1][1] < arr2[p2][0]):
            p1 +=1
        elif(arr2[p2][1] < arr1[p1][0]):
            p2 +=1
        else:
            a3 = findIntersection(arr1[p1],arr2[p2])
            res.append(a3)
            if(a3[1] == arr1[p1][1]):
                p1 +=1
            else:
                p2 +=1
    
    return res

def findIntersection(a1, a2):
    if(a1[0] >= a2[0]):
        lboundary = a1[0]
    else:
        lboundary = a2[0]
    if(a1[1] <= a2[1]):
        rboundary = a1[1]
    else:
        rboundary = a2[1]
    return [lboundary,rboundary]

run_tests()

