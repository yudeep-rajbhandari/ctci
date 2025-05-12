def run_tests():
  tests = [
      # Example from the book
      (list("badreview"), list("reviewbad")),
      # Additional test cases
      ([], []),
      (list("abc"), list("bca")),
      (list("abcdef"), list("cdefab")),
      (list("123456789"), list("456789123")),
      (list("aaabbbccc"), list("bbbcccaaa")),
  ]
  for arr, want in tests:
    arr_copy = arr.copy()  # Make a copy since swap_prefix_suffix modifies in place
    swap_prefix_suffix(arr_copy)
    assert arr_copy == want, f"\nswap_prefix_suffix({arr}): got: {
        arr_copy}, want: {want}\n"

def swap_prefix_suffix(arr):
    l , r = 0 , len(arr) -1
    while(l < r):
        arr[l] , arr[r] = arr[r] , arr[l]
        l +=1
        r -=1
    l ,r = int(len(arr) * 2/3) ,  len(arr) -1
    while(l < r):
        arr[l] , arr[r] = arr[r] , arr[l]
        l +=1
        r -=1
    l ,r = 0, int(len(arr) * 2/3) -1 
    while(l < r):
        arr[l] , arr[r] = arr[r] , arr[l]
        l +=1
        r -=1
    return arr
       
     

# 3 pass :  reverse first 3 

run_tests()
