# Trie -> Prefix Tree
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    # https://leetcode.com/problems/implement-trie-prefix-tree/discuss/320224/Simple-Python-solution
    ## difficult to implement recursive way
    def delete(self, word):
        def recursive(node, word, i):
            if i == len(word):
                if not node.word:
                    return False  # word is not in trie
                node.word = False  # delete word via changing isEnd be False
                return len(node.children) == 0  # return whether it has no children
            if word[i] not in node.children:  # word is not in trie
                return False
            need_delete = recursive(node.children[word[i]], word, i + 1)
            if need_delete:
                node.children.pop(word[i])
                return len(node.children) == 0
            return False  # current node still has other chars, don't need to delete it

        recursive(self.root, word, 0)


    def deleteIteratively(self, word):
        node = self.root
        beforeDelete = None

        if not word: return False

        for char in word:
            if char not in node.children:
                return False

            if len(node.children) == 1:
                pass


        pass

    # https://leetcode.com/problems/implement-trie-prefix-tree/discuss/631423/python3-bonus-delete-function
    '''
    /** Deletes a word from the trie if present, and return true if the word is deleted successfully. */
    public boolean delete(String word) {
        if (word == null || word.length() == 0) {
            return false;
        }
        
        // All nodes below 'deleteBelow' and on the path starting with 'deleteChar' (including itself) will be deleted if needed
        TrieNode deleteBelow = null;
        char deleteChar = '\0';
        
        // Search to ensure word is present
        TrieNode parent = root;
        for (int i = 0; i < word.length(); i++) {
            char cur = word.charAt(i);
            
            TrieNode child = parent.children.get(cur); // Check if having a TrieNode associated with 'cur'
            if (child == null) { // null if 'word' is way too long or its prefix doesn't appear in the Trie
                return false;
            }
            
            if (parent.children.size() > 1 || parent.isEndOfWord) { // Update 'deleteBelow' and 'deleteChar'
                deleteBelow = parent;
                deleteChar = cur;
            }
            
            parent = child;
        }
        
        if (!parent.isEndOfWord) { // word isn't in trie
            return false;
        }
        
        if (parent.children.isEmpty()) {
            deleteBelow.children.remove(deleteChar);
        } else {
            parent.isEndOfWord = false; // Delete word by mark it as not the end of a word
        }
        
        return true;
    }
    '''