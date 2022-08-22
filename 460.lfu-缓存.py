#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#

# @lc code=start
class LFUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._key_to_val = {}
        self._key_to_freq = {}
        self._freq_to_keys = {}
        self._min_freq = 0

    def get(self, key: int) -> int:
        if key not in self._key_to_val:
            return -1
        self._increase_freq(key)
        return self._key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return None
        if key in self._key_to_val:
            self._key_to_val[key] = value
            self._increase_freq(key)
            return
        if len(self._key_to_val) == self._capacity:
            self._remove_min_freq()
        self._key_to_val[key] = value
        self._key_to_freq[key] = 1
        if 1 not in self._freq_to_keys:
            self._freq_to_keys[1] = collections.OrderedDict()
        self._freq_to_keys[1][key] = None
        self._min_freq = 1

    def _increase_freq(self, key: int) -> None:
        freq = self._key_to_freq[key]
        self._key_to_freq[key] += 1

        # key从freq到freq+1
        self._freq_to_keys[freq].pop(key)
        if freq + 1 not in self._freq_to_keys:
            self._freq_to_keys[freq + 1] = collections.OrderedDict()
        # 字典当set用
        self._freq_to_keys[freq + 1][key] = None

        # 处理min_freq
        if not self._freq_to_keys[freq]:  # 原freq为空
            self._freq_to_keys.pop(freq)
            if freq == self._min_freq:  # 且该freq为最小
                self._min_freq += 1

    def _remove_min_freq(self) -> None:
        key, _ = self._freq_to_keys[self._min_freq].popitem(last=False)
        self._key_to_val.pop(key)
        self._key_to_freq.pop(key)
        if not self._freq_to_keys[self._min_freq]:
            self._freq_to_keys.pop(self._min_freq)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
