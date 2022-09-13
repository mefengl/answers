#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#
import bisect
import collections
from typing import List


# @lc code=start
def left_search(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (r - l) // 2 + l
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] == target:
            r = mid - 1
    return l


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dd = collections.defaultdict(list)
        res = 0
        for i, c in enumerate(s):
            dd[c].append(i)
        for word in words:
            begin_index = -1
            for i, c in enumerate(word):
                # left_search是
                # 手动实现
                target_index = left_search(dd[c], begin_index)
                # Python内置
                # target_index = bisect.bisect_left(dd[c],begin_index)
                if target_index == -1 or target_index == len(dd[c]):
                    break
                # dd中存储的便是s的索引数组
                begin_index = dd[c][target_index] + 1
                # 全部搜索到
                if i == len(word) - 1:
                    res += 1
        return res


# if __name__ == "__main__":
#     Solution().numMatchingSubseq("abcde" ,["a","bb","acd","ace"])

# @lc code=end
