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
    length = len(arr)
    n = int(length/3)
    nn = int(length * 2/3)
    l , m , r = 0, n , nn
    while(r < length):
        arr[l] , arr[m] = arr[m], arr[l]
        arr[m], arr[r] = arr[r] , arr[m]
        l +=1
        r +=1
        m +=1
    return arr

# 3 pass :  reverse first 3 

run_tests()
