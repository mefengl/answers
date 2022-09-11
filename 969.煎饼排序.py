#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#

# @lc code=start
def reverse(arr: List[int], i: int, j: int) -> None:
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def flip(arr: List[int], n: int, res: List[int]) -> None:
    if n == 0:
        return
    max_cake = 0
    max_index = 0
    for i in range(n):
        if arr[i] > max_cake:
            max_cake = arr[i]
            max_index = i
    # 最大的煎饼翻到最上面
    reverse(arr, 0, max_index)
    # +1因为翻转从1计数
    res.append(max_index + 1)
    # 再翻转到最下面
    reverse(arr, 0, n - 1)
    # len是从1计数的
    res.append(n)
    flip(arr, n - 1, res)


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        flip(arr, len(arr), res)
        return res


# @lc code=end
