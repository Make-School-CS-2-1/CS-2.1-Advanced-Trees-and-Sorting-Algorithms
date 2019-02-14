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

  def add_word(self, word):
    # print('INSERTING WORD', word)
    # Set current node to the root node
    curr_node = self.root
    # Iterate over the letters in the word
    for i, letter in enumerate(word):
      found_letter = False
      # Look at all the children of the currrent node
      for j, node in enumerate(self[curr_node]):
        # If the node's letter and the current letter are the same
        if node[0] == letter:
          # print('found letter', letter)
          # If this is the last letter of the word and this word is not already inserted into the Trie
          if i == len(word) - 1 and not node[2]:
            # Edit the current node to represent the end of a word
            self[curr_node][j] = (curr_node[0], curr_node[1], True)
            # Set the curr nide to this edited node
            # Note: we can't set curr_node to node because node is a copy of the node not a reference, so it holds the oriignal data not the edited
            curr_node = self[curr_node][j]
            # Create a new key from the edited node and assign it the keys from the old node while simultaneously removing that key
            self[curr_node] = self.pop(node)
          # If this is not the last letter of the word
          else:
            # Set the current node to node, walking down the path of the word by one letter
            curr_node = node
          found_letter = True
          # Iterate to the next letter
          break;
      if not found_letter:
        # print('did not find letter', letter)
        # If this is the last letter in the word
        if i == len(word) - 1:
          # Create a new node that marks the end of a word
          new_node = (letter, self.id, True)
        else:
          # Create a new node
          new_node = (letter, self.id, False)
        # increment id
        self.id += 1
        # Add the new node as a child of the current node
        self[curr_node].append(new_node)
        # Make the new node a parent in the dictionary
        self[new_node] = []
        # Make the new node the curr node
        curr_node = new_node
    
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
        # print(node)
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