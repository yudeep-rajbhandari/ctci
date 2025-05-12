def run_tests():
  tests = [
      # Example 1 from the book
      (list("seekerandwriter"), "edit", list("sekeranwreredit")),
      # Example 2 from the book
      (list("bacb"), "ab", list("bcab")),
      # Example 3 from the book
      (list("babc"), "b", list("abcb")),
      # Additional test cases
      ([], "", []),
      (list("a"), "a", list("a")),
      (list("abc"), "", list("abc")),
      (list("hello"), "ho", list("ellho")),
      (list("abcabc"), "abc", list("abcabc")),
  ]
  for arr, word, want in tests:
    arr_copy = arr.copy()  # Make a copy since move_word modifies in place
    move_word(arr_copy, word)
    assert arr_copy == want, f"\nmove_word({arr}, {word}): got: {
        arr_copy}, want: {want}\n"
def move_word(arr, word):
    s, w = len(arr) - 1 , len(arr) - 1
    wordS = len(word) -1
  
    while(wordS > 0):
        print(s)
        if(arr[s] == word[wordS]):
            arr[s], arr[w] = arr[w], arr[s]
            wordS -= 1
            w -=1
        s -=1
    return arr

run_tests()
