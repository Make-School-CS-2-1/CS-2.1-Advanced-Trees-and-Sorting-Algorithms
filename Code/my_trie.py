#!python

class MyTrie(dict):

  def __init__(self, word_list=None):
    super(MyTrie, self).__init__()

    self.id = 0
    self.root = ('', self.id, False)
    self[self.root] = []
    self.id += 1

    if word_list is not None:
      for word in word_list:
        self.add_word(word)


  def add_word(self, word):
    print('INSERTING WORD', word)
    # Set current node to the root node
    curr_node = self.root
    # Iterate over the letters in the word
    for letter in word:
      found_letter = False
      # Look at all the children of the currrent node
      for node in self[curr_node]:
        # If the node's letter and the current letter are the same
        if node[0] == letter:
          print('found letter', letter)
          # mark the found node as the current node
          curr_node = node
          found_letter = True
          if letter == word[-1]:
            curr_node[2] = True
          # Iterate to the next letter
          break;
      if not found_letter:
        print('did not find letter', letter)
        # Create the new node as a child of curr_node
        if letter == word[-1]:
          new_node = (letter, self.id, True)
        else:
          new_node = (letter, self.id, False)
        # increment id
        self.id += 1
        # Add the new node as a child of the current node
        self[curr_node].append(new_node)
        # Make the new node a parent in the dictionary
        self[new_node] = []
        # Make the new node the curr node
        curr_node = new_node
    # After inserting all the letters into the trie,
    #   mark the last node as the terminal node in a word
    self[(curr_node[0], curr_node[1], True)] = self.pop(curr_node)
    
  def find_words_from_node(self, words, prefix='', node=None):
    # If no node is specififed, start from node
    if not node:
      node = self.root

    if node[2]:
      words.append(prefix)

    for child in self[node]:
      print('child', child)
      new_prefix = prefix + child[0]
      self.find_words_from_node(words, new_prefix, child)
      

  def autocomplete(self, prefix):
    words = []
    curr_node = self.root
    
    # Find the node representing the last letter in prefix
    # Iterate over all letters in prefix
    for letter in prefix:
      found_letter = False
      # Look at all children of current node
      for node in self[curr_node]:
        # When the letter is found
        if node[0] == letter:
          # Update curr node to current node
          curr_node = node
          found_letter = True
          break;
      # If the prefix isn't in the trie that means there won't be anything to suggest
      if not found_letter:
        return
    
    # curr node will be the base for any complete word based on prefix
    base_node = curr_node
    self.find_words_from_node(words, prefix, base_node)
    return words
    

if __name__ == "__main__":
  import sys
  test_words = ['ape', 'apple', 'apricot', 'dog', 'ditch', 'doctor']
  # test_words = ['ape']
  test_trie = MyTrie(test_words)
  # print(test_trie)
  print(test_trie.autocomplete('ap'))