# Python Trie Traversal

Python implementation of trie traversal. Search a string (e.g. HTML file) containing millions of characters for matches within a trie tree containing millions of words in less than 0.5 seconds.

### Description

Generates a random list of strings that are added to the trie. Adds two sample strings that are contained in the sample HTML. Fetches sample HTML from Dropbox. Searches HTML using trie data and outputs the result. The result contains the match with its start/end index within the HTML.

**Sample output**

Sample output for a trie tree of 10,000,000 words searching a HTML document of 2,500,000 characters.

```console

Generating a random list...

Searching trie...

Result: [{'result': 'HU6630B', 'start_index': 750603, 'end_index': 750610}]

Search time: 0.11101756499920157 seconds

```

**Trie & Node logic**

```python
class Node:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}


class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        Initialize trie with at least 1 root node. It has no character
        """
        self.root = Node("")

    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        for char in word:
            # Check if char currently exists in any of the root node's children
            if char in node.children:
                # If a node for this char already exists, create a new child.
                # When we do "node = node.children[char]", we are moving down
                # the trie tree
                node = node.children[char]
            else:
                # If a character is not found, create a new node in the trie
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word when all characters are looped
        node.is_end = True

    def dfs(self, node, query):
        """
        Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - query: the search query
        """
        # As the trie is traversed, characters from each of the matching nodes
        # are appended to the "match" string
        match = ""

        for char in query:
            if char in node.children:
                # A node exists with this char
                match += char

                # Move down to the next node
                node = node.children[char]

                # At the end of the trie and the word is complete, return match
                if node.is_end:
                    return match
            else:
                # cannot find a match on first depth, return None
                return

    def query(self, str):
        """
        Given an input, retrieve all words in the trie that match the input
        """
        # Start at the root node
        node = self.root

        match = self.dfs(node, str)

        return match
```

### How to run

Create a virtual environment.

```sh

python -m venv env

```

Install dependencies found in `requirements.txt`.

```sh

pip install -r requirements.txt

```

Run main.py

```sh

python main.py

```

### Benchmark on my PC:

**10,000,000 strings, 100,000 sample HTML: 0.561 seconds**
