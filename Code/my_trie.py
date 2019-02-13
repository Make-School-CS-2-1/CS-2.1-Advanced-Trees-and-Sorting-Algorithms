#!python

class MyTrie(dict):

  def __init__(self, word_list=None):
    super(MyTrie, self).__init__()

    self.id = 0
    # the charcter, a unique id, end charcter in a word
    self.root = ('', self.id, False)
    self[self.root] = []
    self.id += 1

    if word_list is not None:
      for word in word_list:
        self.add_word(word)

# a -> p
# p -> e

  def add_word(self, word):
    # print('INSERTING WORD', word)
    # Set current node to the root node
    curr_node = self.root
    # Iterate over the letters in the word
    for i, letter in enumerate(word):
      found_letter = False
      # Look at all the children of the currrent node
      for node in self[curr_node]:
        # If the node's letter and the current letter are the same
        if node[0] == letter:
          # print('found letter', letter)
          # mark the found node as the current node
          if i == len(word) - 1 and not node[2]:
            self[curr_node][i] = (curr_node[0], curr_node[1], True)
            curr_node = self[curr_node][i]
            self[curr_node] = self.pop(node)
          else:
            curr_node = node
          found_letter = True
          # Iterate to the next letter
          break;
      if not found_letter:
        # print('did not find letter', letter)
        # Create the new node as a child of curr_node
        # if letter == word[-1]:
        if i == len(word) - 1:
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
      new_prefix = prefix + child[0]
      self.find_words_from_node(words, new_prefix, child)
      

  def autocomplete(self, prefix):
    # print('Looking for prefix:', prefix)
    # print('root', self[self.root])
    words = []
    curr_node = self.root
    
    # Find the node representing the last letter in prefix
    # Iterate over all letters in prefix
    for letter in prefix:
      # print('looking for letter:', letter)
      found_letter = False
      # Look at all children of current node
      for node in self[curr_node]:
        print(node)
        # When the letter is found
        if node[0] == letter:
          # print('found letter (', letter, ') in node:', node)
          # Update curr node to current node
          curr_node = node
          found_letter = True
          break;
      # If the prefix isn't in the trie that means there won't be anything to suggest
      if not found_letter:
        print('PREFIX NOT IN TRIE')
        return words
    
    # curr node will be the base for any complete word based on prefix
    base_node = curr_node
    self.find_words_from_node(words, prefix, base_node)
    return words
    

if __name__ == "__main__":
  import sys
  test_words = ['ap', 'ape', 'apple', 'apricot', 'ap', 'dog', 'ditch', 'doctor', 'map', 'mark', 'mat', 'mattress', 'matter', 'mobile','call', 'cat', 'category']
  # test_words = ['mat', 'mattress']
  test_trie = MyTrie(test_words)
  print(test_trie)
  print(test_trie.autocomplete('m'))