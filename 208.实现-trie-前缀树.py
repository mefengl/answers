#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:
    def __init__(self):
        self._trie = {}

    def insert(self, word: str) -> None:
        t = self._trie
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t["-"] = True

    def search(self, word: str) -> bool:
        t = self._trie
        for char in word:
            if char not in t:
                return False
            t = t[char]
        return "-" in t

    def startsWith(self, prefix: str) -> bool:
        t = self._trie
        for char in prefix:
            if char not in t:
                return False
            t = t[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
