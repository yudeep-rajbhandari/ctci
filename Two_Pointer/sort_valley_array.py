def run_tests():
  tests = [
      # Example 1 from the book
      ([8, 4, 2, 6], [2, 4, 6, 8]),
      # Example 2 from the book
      ([1, 2], [1, 2]),
      # Example 3 from the book
      ([2, 2, 1, 1], [1, 1, 2, 2]),
      # Additional test cases
      ([], []),
      ([1], [1]),
      ([3, 2, 1, 4], [1, 2, 3, 4]),
      ([5, 4, 3, 2, 1, 2, 3], [1, 2, 2, 3, 3, 4, 5]),
      ([1, 1, 1, 1], [1, 1, 1, 1]),
  ]
  for arr, want in tests:
    got = sort_valley_array(arr)
    assert got == want, f"\nsort_valley_array({arr}): got: {got}, want: {want}\n"

def sort_valley_array(arr):
    center = 0
    finalArr = []
    for i in range(len(arr)):
        if(i == len(arr)-1):
            center = i
            finalArr.append(arr[i])
            break
        if(arr[i] < arr[i+1]):
            center = i
            finalArr.append(arr[i])
            break
        
    l , r = center-1,center+1
    while(l >= 0 and r < len(arr)):
        if(arr[l] <= arr[r]):
            finalArr.append(arr[l])
            l -=1
        else:
            finalArr.append(arr[r])
            r +=1
    
    if(l >=0):
        while(l >=0):
            finalArr.append(arr[l])
            l -=1
    if(r < len(arr)):
        while(r < len(arr)):
            finalArr.append(arr[r])
            r +=1
    return finalArr

run_tests()
        

        
    

    

# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Sort Valley Shaped Array

# A *valley-shaped* array is an array of integers such that:

# - It can be split into a non-empty prefix and a non-empty suffix
# - The prefix is sorted in decreasing order (duplicates allowed)
# - The suffix is sorted in increasing order (duplicates allowed)

# Given a valley-shaped array, `arr`, return a new array with the elements sorted.

# ```
# Example 1: arr = [8, 4, 2, 6]
# Output:  [2, 4, 6, 8]
# Explanation: Note that the decreasing prefix is not necessarily unique. The decreasing prefix could be [8, 4] or [8, 4, 2]. The corresponding increasing suffixes would be [2, 6] or [6].

# Example 2: arr = [1, 2]
# Output:  [1, 2]. The array is already sorted (the decreasing prefix is just [1]).

# Example 3: arr = [2, 2, 1, 1]
# Output:  [1, 1, 2, 2]
# ```

# Constraints:

# - 0 ≤ arr.length ≤ 10^6
# - -10^9 ≤ arr[i] ≤ 10^9