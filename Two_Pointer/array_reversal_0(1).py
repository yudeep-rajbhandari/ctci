def run_tests():
  tests = [
      # Test cases
      (list("hello"), list("olleh")),
      (list(""), list("")),
      (list("a"), list("a")),
      (list("ab"), list("ba")),
      (list("abc"), list("cba")),
      (list("abcd"), list("dcba")),
      (list("12345"), list("54321")),
  ]
  for arr, want in tests:
    arr_copy = arr.copy()  # Make a copy since reverse modifies in place
    reverse(arr_copy)
    assert arr_copy == want, f"\nreverse({arr}): got: {
        arr_copy}, want: {want}\n"

def reverse(arr):
    l , r = 0, len(arr)-1
    while(l < r):
        arr[l], arr[r] = arr[r], arr[l]
        l +=1
        r -=1
    return arr

run_tests()