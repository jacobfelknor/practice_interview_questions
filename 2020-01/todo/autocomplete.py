# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query
# string s and a set of all possible query strings, return
# all strings in the set that have s as a prefix.

# For example, given the query string de and the set of
# strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more
# efficient data structure to speed up queries.


# Trie data structure reference: https://www.geeksforgeeks.org/trie-insert-and-search/


class TrieNode:
    def __init__(self):
        # the list represents each letter of the alphabet.
        # It will hold a TrieNode instance if that is the next
        # letter of a string
        self.children = [None] * 26
        # record if this letter is the end of the word
        self.end = False


class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        # return a new trie node with null children
        return TrieNode()

    def _char_index(self, ch):
        # private helper function
        # Converts key current character into index
        # a --> 0, b --> 1, ...., z --> 25
        return ord(ch) - ord("a")

    def insert(self, key):
        # Walk through levels of tree
        # If current character at current level is not present, add it

        # If we make it through entire string without creating a new node,
        # we simply mark the node as the end of a word
        current = self.root
        length = len(key)
        for level in range(length):
            index = self._char_index(key[level])

            # if current character is not present
            if not current.children[index]:
                current.children[index] = self.get_node()
            current = current.children[index]

        # mark last node as leaf
        current.end = True

    def search(self, key):
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        current = self.root
        length = len(key)
        for level in range(length):
            index = self._char_index(key[level])
            if not current.children[index]:
                return False
            current = current.children[index]

        return current != None and current.end


class AutoComplete:
    def __init__(self, bank):
        # for brute force solution:
        self.bank = bank

        # for trie data structure solution:
        self.trie = Trie()
        for x in bank:
            self.trie.insert(x)

    def brute_query(self, s):
        length = len(s)
        ret = []
        for ii in range(len(self.bank)):
            check = True
            for y in range(length):
                if self.bank[ii][y] != s[y]:
                    check = False
            if check:
                ret.append(self.bank[ii])
        print(ret)
        return ret

    def trie_query(self, s):
        print(self.trie.search("deer"))


if __name__ == "__main__":
    testcase = AutoComplete(["dog", "deer", "deal"])

    testcase.trie_query("de")
