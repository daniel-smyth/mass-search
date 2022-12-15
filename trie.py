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


class TrieTool:
    """The tagger class to query the trie"""

    def __init__(self, strings):
        """
        Initialize tagger by adding words to trie.
        """
        self.trie = Trie()

        for string in strings:
            self.trie.insert(string)

    def tag_string(self, html):
        """
        Given a HTML string, locate if any of the strings that appear in the
        HTML. Returning their start and end index in the HTML.
        """
        output = []

        # Split HTML into words to loop through
        words = html.split(" ")

        for words in words:
            search_result = self.trie.query(words)

            if search_result is not None:
                start_index = html.find(search_result)
                output.append(
                    {
                        "result": search_result,
                        "start_index": start_index,
                        "end_index": start_index + len(search_result),
                    }
                )

        return output
