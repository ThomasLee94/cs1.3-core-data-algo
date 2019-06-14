from set import Set

# Test case
# list_1 = ['a','a','b','c']
# list_2 = ['c','d','e']
# expected_outcome = ['a', 'a', 'b']

# convert banned_word into set for constant look-up
# iterate through list_1
  # compare with elements in list_2 by iterating
    # create new list
    # put in non duplicated elements in new list

def redact_words(words, banned_words):
  # ! Runtime = O(n), n being the length of words
  # ! looking up in set is constant time
  
  banned_words_set = Set(banned_words)
  output = list()
  for word in words:
    if word not in banned_words_set:
      output.append(word)
  return output


