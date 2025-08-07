from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise TypeError("Input must be a list of strings")

        if not strings or len(strings) == 0:
            return ""

        for i, word in enumerate(strings):
            self.put(word, i)

        def _find(node, prefix):
            if len(node.children.keys()) > 1 or (node.value is not None):
                return prefix
            for char, next_node in node.children.items():
                prefix += char
                result = _find(next_node, prefix)
                return result
        prefix = ""
        return _find(self.root, prefix)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    print(trie.find_longest_common_word(strings))
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print(trie.find_longest_common_word(strings))
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    print(trie.find_longest_common_word(strings))
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["a"]
    print(trie.find_longest_common_word(strings))
    assert trie.find_longest_common_word(strings) == "a"

    trie = LongestCommonWord()
    strings = []
    print(trie.find_longest_common_word(strings))
    assert trie.find_longest_common_word(strings) == ""