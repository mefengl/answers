#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class Node:
    """双向节点"""

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoubleList:
    """双向链表"""

    def __init__(self):
        self._size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addLast(self, node: Node) -> None:
        # 加入节点
        node.prev = self.tail.prev
        node.next = self.tail
        # 其它节点修改
        self.tail.prev.next = node
        self.tail.prev = node
        self._size += 1

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    # 常用操作封装，等于remove(head.next)
    def removeFirst(self) -> Node:
        if self._size == 0:
            return None
        first = self.head.next
        self.remove(first)
        return first

    @property
    def size(self) -> int:
        return self._size


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._map = {}
        self._cache = DoubleList()

    # key存在下的刷新
    def makeRecently(self, key: int) -> None:
        node = self._map[key]
        self._cache.remove(node)
        self._cache.addLast(node)

    def addRecently(self, key: int, value: int) -> None:
        node = Node(key, value)
        self._map[key] = node
        self._cache.addLast(node)

    # 用于put中键存在的情况下，清除某指定的key
    def deleteKey(self, key: int) -> None:
        node = self._map[key]
        self._cache.remove(node)
        self._map.pop(key)

    # 用于容量已满，添加新键的情况，此时不知道key
    def removeLeastRecently(self) -> None:
        deleteNode = self._cache.removeFirst()
        self._map.pop(deleteNode.key)

    def get(self, key: int) -> int:
        if key not in self._map:
            return -1
        self.makeRecently(key)
        return self._map[key].value

    def put(self, key: int, value: int) -> None:
        if key in self._map:
            self.deleteKey(key)
            self.addRecently(key, value)
            # 到此已经完成，不可往下了
            return
        if self._cache.size == self._capacity:
            self.removeLeastRecently()
        # 至少有1个容量剩余
        self.addRecently(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
