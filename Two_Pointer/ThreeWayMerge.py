import math
def run_tests():
  tests = [
      # Example from the book
      ([2, 3, 3, 4, 5, 7], [3, 3, 9], [3, 3, 9], [2, 3, 4, 5, 7, 9]),
      # Additional test cases
      ([], [], [], []),
      ([1], [], [], [1]),
      ([1], [1], [1], [1]),
      ([1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 2, 3, 4, 5]),
      ([1, 1, 1], [1, 1], [1], [1]),
      ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
  ]
  for arr1, arr2, arr3, want in tests:
    got = three_way_merge(arr1, arr2, arr3)
    assert got == want, f"\nthree_way_merge({arr1}, {arr2}, {arr3}): got: {
        got}, want: {want}\n"

def three_way_merge(arr1, arr2, arr3):
    p1 , p2, p3 = 0, 0 , 0
    finalArr = []
   
    while(p1 < len(arr1) or p2 < len(arr2) or p3 < len(arr3)):
        currentMin = math.inf
        if(p1 < len(arr1) and arr1[p1] <= currentMin):
            if(arr1[p1] < currentMin):
                currentMin = arr1[p1]
            p1 +=1
        if(p2 < len(arr2) and arr2[p2] <= currentMin):
            if(arr2[p2] < currentMin):
                currentMin = arr2[p2]
            p2 +=1
        if(p3 < len(arr3) and arr3[p3] <= currentMin):
            if(arr3[p3] < currentMin):
                currentMin = arr3[p3]
            p3 +=1
        if(len(finalArr) == 0):
            finalArr.append(currentMin)
        else:
            if(currentMin > finalArr[-1]):
                finalArr.append(currentMin)
            

    return finalArr

run_tests()

        
        


