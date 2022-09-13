# leetcode

## [354 俄罗斯套娃信封问题](https://leetcode.cn/problems/russian-doll-envelopes/)

二维平面的最长子序列问题

> 宽度升序，保证一维包含
>
> 高度降序，保证二维不包含重复宽度（同样宽度下，高度前面的高度只可能比它大，所以不会重复）

参考：https://labuladong.github.io/article/fname.html?fname=动态规划设计：最长递增子序列

## [34 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

区间的裁剪

参考：https://labuladong.github.io/article/fname.html?fname=二分查找详解

## [77 组合](https://leetcode.cn/problems/combinations/)

k 个元素的组合是子集树的 k 层节点

> len(val)决定层数，而不是 num(idx+1)，那只是选择

参考：https://labuladong.github.io/article/fname.html?fname=子集排列组合

## [90 子集 II](https://leetcode.cn/problems/subsets-ii/)

值相同的相邻树枝会产生重复

> 排序，num[i-1] != num[i]

参考：https://labuladong.github.io/article/fname.html?fname=子集排列组合

## [47 排列 II](https://leetcode.cn/problems/permutations-ii/)

左相邻元素没有用过就跳过

> 相同元素相对位置固定，2 -> 2' -> 2''

参考：https://labuladong.github.io/article/fname.html?fname=子集排列组合

## [21 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)

把较小的节点接到结果链表上

参考：https://labuladong.github.io/article/fname.html?fname=链表技巧

## [19 删除链表的倒数第 N 个节点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

双指针构成一条定长绳

参考：https://labuladong.github.io/article/fname.html?fname=链表技巧

## [876 中间值](https://leetcode.cn/problems/middle-of-the-linked-list/)

一步两步

参考：https://labuladong.github.io/article/fname.html?fname=链表技巧

## [160 两个链表的第一个公共节点](https://leetcode.cn/problems/intersection-of-two-linked-lists/)

a+b=b+a

## [76 最小路径和](https://leetcode.cn/problems/minimum-ascent-path/)

right 可行解，left 局部最优解

参考：https://labuladong.github.io/article/fname.html?fname=滑动窗口技巧进阶

## [567 字符串的排列](https://leetcode.cn/problems/permutation-in-string/)

True: 长度和 valid

参考：https://labuladong.github.io/article/fname.html?fname=滑动窗口技巧进阶

## [3 最长无重复字符的子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

不需要 need 的滑动窗口

参考：https://labuladong.github.io/article/fname.html?fname=滑动窗口技巧进阶

## [206 链表反转](https://leetcode.cn/problems/reverse-linked-list/)

last = self.reverseList(head.next)

参考：https://labuladong.github.io/article/fname.html?fname=递归反转链表的一部分

## [92 链表反转 II](https://leetcode.cn/problems/reverse-linked-list-ii/)

successor 相当与链表全反最后的 null，调到开始处，反转前 k 个

参考：https://labuladong.github.io/article/fname.html?fname=递归反转链表的一部分

## [25 反转链表中的每个组](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

不停地反转前 k 个

参考：https://labuladong.github.io/article/fname.html?fname=k个一组反转链表

## [1109 公司飞机票](https://leetcode.cn/problems/corporate-flight-bookings/)

[a,b] -> [a,b-a] -> [a,(b-a)+a]

[a,b] -> [a+3,b-a] -> [a+3,(b-a)+(a+3)]

> 从而完成加一个元素就提供了加一串数组的方法

参考：https://labuladong.github.io/article/fname.html?fname=差分技巧

## [1094 公司可用车辆](https://leetcode.cn/problems/car-pooling/)

同拆分数组，但先下后上

参考：https://labuladong.github.io/article/fname.html?fname=差分技巧

## [48 旋转图像](https://leetcode.cn/problems/rotate-image/)

先后沿斜和竖对称翻转

参考：https://labuladong.github.io/article/fname.html?fname=花式遍历

## [54 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)

四指针

> 每次遍历前的 if 也太不优雅了，但一时间内没有想到更好的解法

参考：https://labuladong.github.io/article/fname.html?fname=花式遍历

## [99 恢复二叉搜索树](https://leetcode.cn/problems/recover-binary-search-tree/)

中序遍历得到仅一对错误的有序数组，通过双指针恢复

参考：插件内 labuladong 思路

## [124 二叉树的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/)

和二叉树宽度类似，但需要将小于 0 的路径置为 0

参考：插件内 labuladong 思路

## [226 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)

left,right=right,left

参考：二叉树递归基本操作：不可中序遍历

## [116 填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)

层遍历

参考：官方题解 方法一：层次遍历

## [114 将二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)

后序遍历，但按照 前序遍历的链表顺序 合并

参考：https://labuladong.github.io/article/fname.html?fname=二叉树系列1

## [654 最大二叉树](https://leetcode.cn/problems/maximum-binary-tree/)

递归

参考：二叉树递归构建基本操作：root(val),root.left=left(),root.right=right()

## [105 根据前序和中序遍历构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

前序遍历的第一个元素是根节点，根节点+中序遍历可以得到左右子树长度，再代入前序遍历

参考：https://labuladong.github.io/article/fname.html?fname=二叉树系列2

## [106 根据中序和后序遍历构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

和 105 一样，小窍门是：inorder 和 postorder 的长度永远是相同的，可以按照它推断索引范围

参考：各序遍历规律

## [889 根据前序和后序遍历构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)

之所以需要中序遍历，是为了确认前序遍历里的第二个元素是左节点还是右节点（当左数长度为 0 时是右节点），此题两种情况都可以

参考：https://labuladong.github.io/article/fname.html?fname=二叉树系列2

## [297 序列化二叉树](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/)

前序后序均可，因为可用特殊符号表示空节点，后序解析时先右树后左树

参考：https://labuladong.github.io/article/fname.html?fname=二叉树的序列化

## [652 检测重复的子树](https://leetcode.cn/problems/find-duplicate-subtrees/)

核心是 297 序列化二叉树，此外就是判断是否已出现且仅出现一次

参考：https://labuladong.github.io/article/fname.html?fname=二叉树系列3

## [912 排序数组](https://leetcode.cn/problems/sort-an-array/)

### 归并排序

\*在后序归并前面已经排好序的数组

参考：https://labuladong.github.io/article/fname.html?fname=归并排序

### 快速排序

在前序将每个元素放在正确的序号位置上

参考：https://labuladong.github.io/article/fname.html?fname=快速排序

## [315 计算右侧小于当前元素的个数](https://leetcode.cn/problems/count-of-smaller-numbers-after-self/)

在每次归并中，前指针和 mid 之间的元素便是「右侧小于当前元素的个数」

参考：https://labuladong.github.io/article/fname.html?fname=归并排序

## [493 翻转对](https://leetcode.cn/problems/reverse-pairs/)

\*比力扣 315 需要的技巧还少些，利用 merge 的同子树只比较一次和合并的两个数组各自是有序的两个特性去做，利用归并排序 merge 中数组有序得到范围解（因为右子树有序，如果 end 比左子树某元素两倍还小，则从 mid+1 到 end 都是解，这样 end-(mid+1)便为解的个数）

参考：https://labuladong.github.io/article/fname.html?fname=归并排序

## [327 计算区间和的个数](https://leetcode.cn/problems/count-of-range-sum/)

前缀和用来快速计算区间和，利用归并排序 merge 中数组有序可以得到范围解（因为右子树有序，根据前缀和的计算方式，在减数不变的情况下，对应的区间和也是有序的，通过 start 排除，通过 end 收纳，则从 start 到 end 都是解，这样 end-start 便为解的个数）

参考：https://labuladong.github.io/article/fname.html?fname=归并排序

## [230 求二叉搜索树的第 k 小元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)

二叉搜索树 中序遍历 升序进行

参考：https://labuladong.github.io/article/fname.html?fname=BST1

## [538 将二叉搜索树转换为累加树](https://leetcode.cn/problems/convert-bst-to-greater-tree/)

二叉搜索树 中序遍历 先右后左 降序进行，维持累加变量并赋值即可

> 二叉搜索树的中序遍历问题往往是有序数组问题

参考：https://labuladong.github.io/article/fname.html?fname=BST1

## [1038 将二叉搜索树转换为累加树](https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/)

同力扣 538，二叉搜索树 中序遍历 先右后左 降序进行，维持累加变量并赋值即可

> 二叉搜索树的中序遍历问题往往是有序数组问题

参考：https://labuladong.github.io/article/fname.html?fname=BST1

## [98 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/)

通过参数，将 root 的约束传递到子孙节点

参考：https://labuladong.github.io/article/fname.html?fname=BST2

## [700 搜索二叉搜索树](https://leetcode.cn/problems/search-in-a-binary-search-tree/)

二分搜索

参考：https://labuladong.github.io/article/fname.html?fname=BST2

## [701 插入二叉搜索树](https://leetcode.cn/problems/insert-into-a-binary-search-tree/)

二分搜索，找到那个空节点，插入

参考：https://labuladong.github.io/article/fname.html?fname=BST2

## [450 删除二叉搜索树节点](https://leetcode.cn/problems/delete-node-in-a-bst/)

二分搜索，找到那个节点，分情况删除，其中左右子节点均有的情况为算法核心，需要取左子树最大或右子树最小（矮子里挑将军是为中庸），然后删除最大值或者最小值节点（妙处在于可以调用正在写的函数）

参考：https://labuladong.github.io/article/fname.html?fname=BST2

## [96 不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/)

左和右子树的组合数乘积就是根节点的组合数

参考：https://labuladong.github.io/article/fname.html?fname=BST3

##[95 不同的二叉搜索树 II](https://leetcode.cn/problems/unique-binary-search-trees-ii/)

\*左和右子树的组合笛卡尔乘积就是根节点的所有组合

参考：https://labuladong.github.io/article/fname.html?fname=BST3

##[215 数组中的第 K 个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)

快速排序的 partition 函数，在这里可以起到二分查找里结果函数的作用（ 类似 nums[mid]，这里是 partition(nums,lo,hi) ）

> 数组可以获得长度，所以第 K 大可以转化成别的东西

## [341 扁平化嵌套列表迭代器](https://leetcode.cn/problems/flatten-nested-list-iterator/)

将头部的非整数变成整数放回去

## [236 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)

两种情况，一种是其中节点就是要找的元素（它本身就是祖先），另一种是节点左右子树都能找到对应元素，这也是祖先（因为需要左右遍历完成，所以后序）

## [1676 二叉树的最近公共祖先-iv](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iv)

> 同力扣 236 题，两种情况，一种是其中节点就是要找的元素（它本身就是祖先），另一种是节点左右子树都能找到对应元素，这也是祖先（因为需要左右遍历完成，所以后序）。

和第一种情况就能直接判断祖先元素一样，不需要所有元素都找到，因为二叉树遍历特点，剩下的元素必然在没有遍历的子树里。

## [1644 二叉树的最近公共祖先-ii](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-ii/)

> 类似力扣 236 与 1676 题

这题的特点是，节点不一定存在，所以无论如何整颗树要遍历完成，所以后序遍历（仍然要及时返回找到的节点，但这里的找到无法决定是否有祖先节点，得根据全局的 flag 判断）

## [235 二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)

由搜索二叉树性质，`p.val <= root.val <= q.val` ，则 root 就是最近公共祖先

## [1650 二叉树的最近公共祖先-iii](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iii/)

类似力扣 160 题，本质是求 两条链表交点

## [222 完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/)

暴力：纯遍历，计算节点个数；
满二叉树：2\*\*n - 1；
完全二叉树：子树是满二叉树（左右高度相同）用满二叉树，子树是普通树（左右高度不同）用纯遍历

## [797 所有可能的路径](https://leetcode.cn/problems/all-paths-from-source-to-target/)

图的遍历等同于多叉树遍历，但需要加上 visited 数组防重复访问，如果需要记录路径，则需要维护路径数组

## [207 课程表](https://leetcode.cn/problems/course-schedule/)

### DFS

从所有节点出发一次，看是否会路径这条蛇是否会咬到自己，咬到代表成环，代表不可能学完

### BFS

不成环的图，从入度为 0 的节点一个个消除，可以消除殆尽

## [210 课程表 II](https://leetcode.cn/problems/course-schedule-ii/)

### DFS

beg->[end]的树结构，后序遍历能保证 beg 们已经访问过了，最后结果需要 reverse

### BFS

消除（popleft）的顺序就是拓扑排序的顺序

## [785 判断二分图](https://leetcode.cn/problems/is-graph-bipartite/)

### DFS

遍历所有子树，没访问过的节点赋反色，访问过的节点检查是否为反色

### BFS

和 DFS 几乎相同，但通过队列来遍历

## [886 可能得二分法](https://leetcode.cn/problems/possible-bipartition/)

和力扣 785 相同，是一个判断二分图的问题，需要将相互讨厌关系转化为图结构

## [323 无向图中连通分量的数目](https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/)

并查集算法，连通分量最大数目是每个节点都是一个子树（通过根节点区分），通过 UNION 函数遍历题目给的边，如果边的两个节点都是一个子树（通过 FIND 找到根节点判别），则不变，如果不是，则将两个节点合并为一个子树（同一个根节点），连通分量减一

参考：https://labuladong.github.io/article/fname.html?fname=UnionFind算法详解

## [130 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)

并查集可以解决，用神圣的 dummy 连接所有 BIG_O，最后没和 dummy 连接的是 BIG_X

参考：https://labuladong.github.io/article/fname.html?fname=UnionFind算法详解

## [990 等式方程的可满足性](https://leetcode.cn/problems/satisfiability-of-equality-equations/)

遍历，如果==，则两个节点必须在一个子树中，连接；
遍历，如果!=，则两个节点必须在不同的子树中（非 is_connected），否则，返回 False

参考：https://labuladong.github.io/article/fname.html?fname=UnionFind算法详解

## [261 以图判树](https://leetcode.cn/problems/graph-valid-tree/)

并查集可以解决，连接所有的边，连接之前，两条边不允许连通，否则返回 False，最后，如果只生成一颗子树（uf.count == 1）返回 True

参考：https://labuladong.github.io/article/fname.html?fname=kruskal

## [1135 最低成本联通所有城市](https://leetcode.cn/problems/connecting-cities-with-minimum-cost/)

### Kruskal

并查集可以解决，核心是将 connections 按 cost 排序，然后逐次连接并更新 cost，连接过的跳过（不然成环，不是树），最后，如果只生成一颗子树（uf.count == 1）返回 True

参考：https://labuladong.github.io/article/fname.html?fname=kruskal

### Prim

从 0 开始，不断切割最短边（优先队列），并切割对应节点（钝刀子），如果最后所有节点都 cut 过，返回 True，否则返回 False

参考：https://labuladong.github.io/article/fname.html?fname=prim算法

## [1584 连接所有点的最小费用](https://leetcode.cn/problems/connecting-cities-with-minimum-cost/)

### Kruskal

并查集可以解决，核心是将 points 转换成带 cost 的 edges，然后逐次连接并更新 cost，连接过的跳过（不然成环，不是树），最后，如果只生成一颗子树（uf.count == 1）返回 True（这一题只会有一个子树）

参考：https://labuladong.github.io/article/fname.html?fname=kruskal

### Prim

基本的 Prim 算法，除此之外，核心是 build_graph，从 0 开始，不断切割最短边（优先队列），并切割对应节点（钝刀子），如果最后所有节点都 cut 过（此题一定全 cut），返回 True，否则返回 False

参考：https://labuladong.github.io/article/fname.html?fname=prim算法

## [743 网络延迟时间](https://leetcode.cn/problems/network-delay-time/)

\*Dijkstra 算法，先建立 graph，然后层序遍历，如果不是更小，就跳过

参考：https://labuladong.github.io/article/fname.html?fname=dijkstra算法

## [1631 最小体力消耗路径](https://leetcode.cn/problems/minimum-energy-cost-to-make-walkable-road/)

Dijkstra 算法，先建立 graph，然后层序遍历，如果不是更小，就跳过。特殊地方在于，一条路径的最大消耗由每一步的最大值而不是总和决定

参考：https://labuladong.github.io/article/fname.html?fname=dijkstra算法

## [1514 概率最大的路径](https://leetcode.cn/problems/path-with-maximum-probability/)

Dijkstra 算法，不过是求最大，所以相应的判断需要取反，另外优先队列需要逆序（压入时加负号，取出时回正也是一个方法）

参考：https://labuladong.github.io/article/fname.html?fname=dijkstra算法

## [277 搜寻名人](https://leetcode.cn/problems/find-the-celebrity/)

擂台制，如果 candidate 认识 other 或者 other 不认识 candidate，candidate 都不可能是名人。最后，candidate 还要和所有人再比一把（防止石头剪刀布式的胜利）

参考：https://labuladong.github.io/article/fname.html?fname=名人问题

## [146 LRU 缓存](https://leetcode.cn/problems/lru-cache/)

\*双向链表+hashmap。LRU 算法要求，双向链表需要实现尾部增，头部删，各处删的方法；另外，需要根据 get 和 put 函数的情况，在中间封装一批函数（总之多做，是有逻辑的）

参考：https://labuladong.github.io/article/fname.html?fname=LRU算法

## [460 LFU 缓存](https://leetcode.cn/problems/lfu-cache/)

\*对 key_to_val/freq、freq_to_keys，还有 min_freq 的同步更新

参考：https://labuladong.github.io/article/fname.html?fname=LFU

## [292 Nim 游戏](https://leetcode.cn/problems/nim-game/)

永远不能是 4 的倍数

参考：labuladong 的算法小抄 5.13.1

## [877 石子游戏](https://leetcode.cn/problems/stone-game/)

先手预定奇数或偶数堆，鉴于共偶数堆且奇数个，先手必赢

参考：labuladong 的算法小抄 5.13.2

## [319 灯泡开关](https://leetcode.cn/problems/bulb-switcher/)

因子问题，亮着的灯泡需要具有两个相同因子，即平方数；故本题为统计 n 前的平方数问题，sqrt 后转 int 即可

参考：labuladong 的算法小抄 5.13.3

## [208 实现 Trie](https://leetcode.cn/problems/implement-trie-prefix-tree/)

前缀树，可以理解为嵌套的字典结构，键为字符，值为字典，如果是叶子节点，值为 true，否则为字典

参考：https://leetcode.com/problems/implement-trie-prefix-tree/discuss/362916

## [191 位 1 的个数](https://leetcode.cn/problems/number-of-1-bits/)

n&(n-1)，每次去掉最低位 1，直到 n 为 0，统计的次数即为 1 的个数

参考：https://labuladong.github.io/article/fname.html?fname=常用的位操作

## [231 2 的幂](https://leetcode.cn/problems/power-of-two/)

2 的幂，只有一个 1，必为最低位，所以去掉最低位 1，一定为 0，即 n&(n-1)==0

参考：https://labuladong.github.io/article/fname.html?fname=常用的位操作

## [136 只出现一次的数字](https://leetcode.cn/problems/single-number/)

> 一个数和它本身做异或运算结果为 0，即 a ^ a = 0；一个数和 0 做异或运算的结果为它本身，即 a ^ 0 = a。

全部异或后，最后一个数即为唯一的数

参考：https://labuladong.github.io/article/fname.html?fname=常用的位操作

## [268 丢失的数字](https://leetcode.cn/problems/missing-number/)

> 一个数和它本身做异或运算结果为 0，即 a ^ a = 0；一个数和 0 做异或运算的结果为它本身，即 a ^ 0 = a。

原有数组和[0-n]数组异或，最后一个数即为唯一的数（注意 0-n 有 n+1 个数）

参考：https://labuladong.github.io/article/fname.html?fname=常用的位操作

## [172 阶乘后的零](https://leetcode.cn/problems/factorial-trailing-zeroes/)

寻找有几对具有 2 因子的因子和具有 5 因子的因子，因为 2 的因子一定比 5 的因子多，所以只需要求出 5 的因子个数即可，自除 5 的和即为结果

参考：https://labuladong.github.io/article/fname.html?fname=阶乘题目

## [793 阶乘函数后 K 个零](https://leetcode.cn/problems/preimage-size-of-factorial-k/)

由力扣 172 题，已知求阶乘尾部 0 个数的方法，该方法可以作为二分法的核心函数，求出左右边界，左右边界中的元素个数即为所求

参考：https://labuladong.github.io/article/fname.html?fname=阶乘题目

## [204 计数质数](https://leetcode.cn/problems/count-primes/)

非素数因子的对称性（sqrt(n)），筛法（if is_prime[idx]），筛法的起始（idx\*idx）

参考：https://labuladong.github.io/article/fname.html?fname=打印素数

## [372 超级次方](https://leetcode.cn/problems/super-pow/)

a^[1,2,k] = a^k _ a^[1,2,k] = a^k _ (a^[1,2])^10

a^k = a^(k-1) \* a # 奇数

a^k = (a^(k/2))^2 # 偶数

参考：https://labuladong.github.io/article/fname.html?fname=superPower

## [645 错误的集合](https://leetcode.cn/problems/set-mismatch/)

\*可以利用异或的性质，a^a = 0，a^0 = a。若是想减小空间复杂度，可以用索引和正负当 dup 和 mis 的标记

参考：https://labuladong.github.io/article/fname.html?fname=缺失和重复的元素

## [382 链表随机指针](https://leetcode.cn/problems/linked-list-random-node/)

蓄水池抽样法，即 1/i _ (1-1/(i+1)) _ (1-1/(i+2)) _ ... _ (1-1/n) = 1/n

参考：https://labuladong.github.io/article/fname.html?fname=水塘抽样

## [398 随机数索引](https://leetcode.cn/problems/random-pick-index/)

蓄水池抽样法，即 1/i _ (1-1/(i+1)) _ (1-1/(i+2)) _ ... _ (1-1/n) = 1/n（会超时，哈希表更快）

参考：https://leetcode.cn/problems/random-pick-index/solution/sui-ji-shu-suo-yin-by-leetcode-solution-ofsq/

## [496 下一个更大元素 I](https://leetcode.cn/problems/next-greater-element-i/)

\*单调栈

参考：https://labuladong.github.io/article/fname.html?fname=单调栈

## [739 每日温度](https://leetcode.cn/problems/daily-temperatures/)

\*单调栈，不过栈内是下一个更大的 index，而不是下一个更大的数字

参考：https://labuladong.github.io/article/fname.html?fname=单调栈

## [503 下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii/)

单调栈，至于循环数组的单调栈，因为单调栈的生成方式便是「下一个」更大的数，那将数组本身连接到数组的「下一个」即可。实质是让「循环的元素逆序提前入栈」，所以通过「索引模 n」的方式来入栈也可以

参考：https://labuladong.github.io/article/fname.html?fname=单调栈

## [239 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/)

\*滑动窗口+单调队列

参考：https://labuladong.github.io/article/fname.html?fname=单调队列

## [232 用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/)

] [

参考：https://labuladong.github.io/article/fname.html?fname=队列实现栈栈实现队列

## [225 用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/)

记录栈顶，有点像把队列当循环队列使用（不能根据记录的栈顶来判断循环是否完成，因为会有重复元素，用队列长度）

参考：https://labuladong.github.io/article/fname.html?fname=队列实现栈栈实现队列

## [355 设计推特](https://leetcode.cn/problems/design-twitter/)

\*OOP，以及优先队列（多关注如何获取最新的 K 条推文）

参考：https://labuladong.github.io/article/fname.html?fname=设计Twitter

## [322 零钱兑换](https://leetcode.cn/problems/coin-change/)

`dp[idx] = min(dp[idx - coin] + 1, dp[idx])`

参考：https://labuladong.github.io/article/fname.html?fname=动态规划详解进阶

## [300 最长上升子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)

最长递增子序列问题，`dp[i] = max(dp[i], dp[j] + 1)`

参考：https://labuladong.github.io/article/fname.html?fname=动态规划设计%EF%BC%9A最长递增子序列

## [354 俄罗斯套娃信封](https://leetcode.cn/problems/russian-doll-envelopes/)

二维最长递增子序列问题，宽度升序，保证一维包含，高度降序，保证二维不包含重复宽度（同样宽度下，高度前面的高度只可能比它大，所以不会重复），求高度的最长递增子序列，时间复杂度 O(n^2)，会超时;
*O(n*log(n))的方法需要借助耐心算法的堆数和二分左搜索

参考：https://labuladong.github.io/article/fname.html?fname=动态规划设计%EF%BC%9A最长递增子序列

## [931 下降路径最小和](https://leetcode.cn/problems/mini-sum-of-path-sum/)

`dp[i][j] = min(dp[i - 1][j - 1], dp[i-1][j], dp[i-1][j + 1]) + matrix[i][j]`（直接 matrix 当 dp 用也可）

参考：常识和动态规划套路

## [72 编辑距离](https://leetcode.cn/problems/edit-distance/)

```
+-----------+-------+
| 替换/跳过 | 插入/ |
+-----------+-------+
| 删除/     | +1/+0 |
+-----------+-------+

+----+----+---+---+---+---+---+
|    | "" | h | o | r | s | e |
+----+----+---+---+---+---+---+
| "" | 0  | 1 | 2 | 3 | 4 | 5 |
+----+----+---+---+---+---+---+
| r  | 1  | 1 | 2 | 3 | 4 | 5 |
+----+----+---+---+---+---+---+
| o  | 2  | 2 | 1 | 2 | 3 | 4 |
+----+----+---+---+---+---+---+
| s  | 3  | 3 | 2 | 2 | 2 | 3 |
+----+----+---+---+---+---+---+

初始值：一个空串变成"",a,ap,app…分别需要0，1，2，3步
```

`dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])`

## [53 最大子数组和](https://leetcode.cn/problems/maximum-subarray/)

dp 值指以序号所在元素为结尾的子数组和，两种状态转移方式，一种是继承，另一种是另起炉灶

`dp[idx] = max(dp[idx] + dp[idx - 1], dp[idx])`

也可用前缀和来写，max_sum = presum[i] - min_presum)

参考：https://labuladong.github.io/article/fname.html?fname=最大子数组

## [1143 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)

`dp[i][j] = dp[i - 1][j - 1] + 1 if text1[i] == text2[j] else max(dp[i - 1][j], dp[i][j - 1])`（字符相同时，取左上角，因为每个字母只能计算一次，如果取上和左的话，其实包含了 text1 或 text2 重复选取的风险；字符不同时，左上角省略，因为它一定不同时大于它的右边和下边）

参考：https://labuladong.github.io/article/fname.html?fname=LCS

## [583 两个字符串的删除操作](https://leetcode.cn/problems/delete-operation-for-two-strings/)

多余字符数 = 总字符数 - 2 * 最长公共子序列长度

参考：https://labuladong.github.io/article/fname.html?fname=LCS

## [712 两个字符串的最小ASCII删除和](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/)

力扣1143和583题解法的综合，即，`最小ASCII删除和 = ASCII总和 - 2 * 最大的公共子序列ASCII和`

参考：https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/discuss/1196499

## [516 最长回文子序列](https://leetcode.com/problems/longest-palindromic-subsequence/)

初始值：`dp[i][i] = 1`，单个字符回文

`dp[i][j] = 2 + dp[i - 1][j - 1] if text[i] == text[j] else max(dp[i][j - 1], dp[i + 1][j])`

dp[i][j]表示以i,j为结尾的最长回文子序列长度，由此可知i < j，且由递推公式可知，需从下往上遍历

参考：https://labuladong.github.io/article/fname.html?fname=子序列问题模板

## [1312 让字符串成为回文串的最小插入次数](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)

最小插入次数 = 字符串长度 - 最长回文子序列长度

参考：https://labuladong.github.io/article/fname.html?fname=子序列问题模板

## [416 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/)

01背包问题，背包容量为sum(nums) // 2

`dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i-1]]`

参考：https://labuladong.github.io/article/fname.html?fname=背包子集

## [518 零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2/)

`dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]`

3种硬币凑出5 = 2个硬币凑出5 + 3种硬币凑出(5-第三个币值) ，后者带来重复选

参考：https://labuladong.github.io/article/fname.html?fname=背包零钱

## [494 目标和](https://leetcode-cn.com/problems/target-sum/)

`dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j + nums[i - 1]]`

j需要从0遍历，nums[i-1]为0的情况下，需要更新值的，因为+0-0都可以凑出0，遍历的话，刚好 dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 0]达到了这一效果

参考：https://labuladong.github.io/article/fname.html?fname=targetSum

## [64 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)

dp初始化中的首行和首列需要转换为grid的前缀和

`dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])`

参考：https://labuladong.github.io/article/fname.html?fname=最小路径和

## [174 地下城游戏](https://leetcode-cn.com/problems/dungeon-game/)

*遍历的是每处的「最小血量」，且需要逆序遍历。注意血量的最小值为1，因为血量为0或负数时，游戏就结束了。

参考：https://labuladong.github.io/article/fname.html?fname=魔塔

## [514 自由之路](https://leetcode-cn.com/problems/freedom-trail/)

状态是指针在ring和key的位置，dp[i][j]表示指针在ring的i位置，key的j位置时，最少需要多少步

`dp[i][j] = min(dp[i][j], dp[i - 1][k] + min(abs(j - k), n - abs(j - k)))`

参考：https://leetcode.cn/problems/freedom-trail/solution/er-xu-cheng-ming-jiu-xu-zui-by-liupengsa-aqk2/

另，递归方法：

参考：https://labuladong.github.io/article/fname.html?fname=转盘

## [787 K 站中转内最便宜的航班](https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/)

*BFS结合优先队列，Dijkstra的思路

参考：https://labuladong.github.io/article/fname.html?fname=旅行最短路径

*DP，状态是剩余步数和当前位置

`dp[t][end] = min(dp[t][end], dp[t - 1][beg] + cost)`

参考：https://leetcode.cn/problems/cheapest-flights-within-k-stops/solution/k-zhan-zhong-zhuan-nei-zui-bian-yi-de-ha-abzi/

## [10 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)

*状态是s的指针和p的指针，dp[i][j]表示i和j前的s和p片段是否匹配

参考：https://leetcode.cn/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/

## [887 鸡蛋掉落](https://leetcode-cn.com/problems/super-egg-drop/)

状态是步数和鸡蛋数，dp[i][j]表示i步j个鸡蛋最多能测多少层

`dp[i][j] = 1 + dp[i - 1][j] + dp[i - 1][j - 1]`

目前O(MN)复杂度的算法，第一个鸡蛋永远是从最高层扔下的，所以，无论碎还是没碎，都能确定最高层（+ 1），如果鸡蛋碎了，那就是少步少蛋（+ dp[i - 1][j - 1]），如果没碎，那就只是少步（+ dp[i - 1][j]）

参考：https://leetcode.com/problems/super-egg-drop/discuss/443089

## [312 戳气球](https://leetcode-cn.com/problems/burst-balloons/)

状态是左右指针，dp[i][j]表示i和j开区间中气球最多能得到多少分，方式是遍历最后一个戳破的气球k（k in [i+1, j-1]）

`dp[i][j] = max(dp[i][j], last_coins(i, k, j) + dp[i][k] + dp[k][j])`

参考：https://labuladong.github.io/article/fname.html?fname=扎气球

## [486 预测赢家](https://leetcode-cn.com/problems/predict-the-winner/)

状态是左右指针，dp[i][j]表示i和j开区间中先手和后手能得到的最大分数

先手后手是相对的，这把的先手是相对于上一把的后手，所以，先手的最大分数是max(先手拿左边 + 后手拿左边，先手拿右边 + 后手拿右边)

参考：https://labuladong.github.io/article/fname.html?fname=动态规划之博弈问题

## [651 4键键盘](https://leetcode-cn.com/problems/4-keys-keyboard/)

状态是总步数，dp[i]表示i步能得到的最多A

`dp[i] = max(dp[i-1] + 1, dp[j - 2] * (i - j + 1))`

参考：https://labuladong.github.io/article/fname.html?fname=动态规划之四键键盘

## [198 打家劫舍](https://leetcode-cn.com/problems/house-robber/)

状态是房子的指针，dp[i]表示偷到第i个房子的最大金额，这里正序逆序均可

`dp[i] = max(dp[i - 1], nums[i - 2] + dp[i - 2])`

nums[i - 2]是因为nums是从0开始的，i是从2开始的，相当于nums[0]前面加了两个0

参考：https://labuladong.github.io/article/fname.html?fname=抢房子

## [213 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/)

同力扣198题，只是多了一个限制，第一间和最后一间不能同时偷，所以，可以分成两种情况，一种是偷第一间，一种是不偷第一间，然后取最大值

参考：https://labuladong.github.io/article/fname.html?fname=抢房子

## [337 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/)


偷与不偷，偷就只能不偷子节点，不偷就能自由选择是否偷子节点

`return (root.val + left[1] + right[1], max(left) + max(right))`

参考：https://leetcode.com/problems/house-robber-iii/discuss/376297

## [121 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

`dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])`

`dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])`

由题，k=1，dp[i - 1][k - 1][0] = dp[i - 1][0][0] = 0

参考：https://labuladong.github.io/article/fname.html?fname=团灭股票问题

## [122 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

`dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])`

`dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])`

由题，k=+∞，dp[i - 1][k - 1][0] = dp[i - 1][k][0]，k不变，可以省略

参考：https://labuladong.github.io/article/fname.html?fname=团灭股票问题

## [309 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

`dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])`

`dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])`

由题，k=+∞，k不变，可以省略，另外，买入需要到卖出的第二天，即：

`dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])`

参考：https://labuladong.github.io/article/fname.html?fname=团灭股票问题

## [714 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

可以在买时，或者是卖时，扣除手续费，这里选择在卖时扣除

`dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i] - fee)`

`dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])`

同样，k=+∞，k不变，可以省略

参考：https://labuladong.github.io/article/fname.html?fname=团灭股票问题

## [123 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)


`dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])`

`dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])`

由题，k = 2

参考：https://labuladong.github.io/article/fname.html?fname=团灭股票问题

## [188 买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)

`dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])`

`dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])`

k > n / 2，可以认为k=+∞

参考：https://labuladong.github.io/article/fname.html?fname=团灭股票问题

## [187 重复的DNA序列](https://leetcode-cn.com/problems/repeated-dna-sequences/)

*滑动窗口，配合 自定义哈希，因为数字可以简单的通过数学运算去除最高位和加入最低位

参考：https://labuladong.github.io/article/fname.html?fname=rabinkarp

## [28 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/)

### Rabin-Karp 算法

*同力扣187题，滑动窗口，配合 自定义哈希，因为数字可以简单的通过数学运算去除最高位和加入最低位，多加一步取模防止数字溢出，取模可能带来重复，所以匹配后还需字符串比较

参考：https://labuladong.github.io/article/fname.html?fname=rabinkarp

### KMP

*建立自动机的转移表，然后遍历字符串，根据转移表，进行状态转移

参考：https://labuladong.github.io/article/fname.html?fname=动态规划之KMP字符匹配算法

## [435 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/)

下一个最早end = start于当前最早end后的最早end

参考：https://labuladong.github.io/article/fname.html?fname=贪心算法之区间调度问题

## [452 用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/)

*同力扣435题，不过边界不能重叠

下一个最早end = start于当前最早end后的最早end

参考：https://labuladong.github.io/article/fname.html?fname=贪心算法之区间调度问题

## [253 会议室 II](https://leetcode-cn.com/problems/meeting-rooms-ii/)

时间线上，遇到start，count+=1，遇到end，count-=1，count的最大值就是所需会议室数

参考：https://labuladong.github.io/article/fname.html?fname=安排会议室

## [1024 视频拼接](https://leetcode-cn.com/problems/video-stitching/)

### 跳跃游戏

`lo, hi = hi, max(max_jumps[lo : hi + 1])`

参考：https://leetcode.com/problems/video-stitching/discuss/484877

### labuladong

用while循环实现了max_jumps[lo:hi + 1]，相对而言比较复杂，更推荐直接采用跳跃游戏的思路

参考：https://labuladong.github.io/article/fname.html?fname=剪视频

## [55 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)

`max_jump = max(max_jump, i + num)`

终止条件是 i > max_jump，或 max_jump < i，这意味着i已经是不可到达的了（不可以是等于，因为等于的话，i还是可以到达的，可以继续运行算法）

参考：https://leetcode.com/problems/jump-game/discuss/20907

## [45 跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/)

和力扣1024相同

`lo, hi = hi, max(max_jumps[lo : hi + 1])`

参考：力扣1024题

## [134 加油站](https://leetcode-cn.com/problems/gas-station/)

*gas和cost构成每一站的变化，只要总和大于0，就一定有解，而且在唯一解的情况下，应该从油气理论的最低点开始

参考：https://labuladong.github.io/article/fname.html?fname=老司机

## [46 全排列](https://leetcode-cn.com/problems/permutations/)

将每个数都放在第一个位置，然后递归求解剩下的数的全排列

参考：https://leetcode.com/problems/permutations/discuss/18296

## [51 N皇后](https://leetcode-cn.com/problems/n-queens/)

行列值的加减结果能确定唯一的斜线

参考：https://leetcode.com/problems/n-queens/discuss/19810

## [1288 删除被覆盖区间](https://leetcode-cn.com/problems/remove-covered-intervals/)

intervals.sort(key=lambda x: (x[0], -x[1]))

排序后，后者只有end比cur_end大，才会被保留

参考：https://leetcode.com/problems/remove-covered-intervals/discuss/878478

## [56 合并区间](https://leetcode-cn.com/problems/merge-intervals/)

b若开始比a结束早，可以更新a的end，否则，将a加入结果集，更新a为b

参考：https://leetcode.com/problems/merge-intervals/discuss/21227

## [986 区间列表的交集](https://leetcode-cn.com/problems/interval-list-intersections/)

*不是没有交集便是有交集，左边的最大值和右边的最小值是交集的左右边界，根据右边界决定哪个区间往后移动

参考：https://labuladong.github.io/article/fname.html?fname=区间问题合集

## [659 分割数组为连续子序列](https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/)

存在num-1的前缀，那么num就可以接在前缀后面

不存在，如果num+1和num+2存在，那么就可以新建一个子序列，否则，返回false

参考：https://labuladong.github.io/article/fname.html?fname=斗地主

## [969 煎饼排序](https://leetcode-cn.com/problems/pancake-sorting/)

将最大的数放在顶上，然后翻转全部，这样就把最大的数放到了最后

参考：https://labuladong.github.io/article/fname.html?fname=烧饼排序

## [43 字符串相乘](https://leetcode-cn.com/problems/multiply-strings/)

i+j+1是个位索引，i+j是十位索引

每次将乘积加上个位索引的值，个位更新个位索引值，进位更新十位索引值

参考：https://labuladong.github.io/article/fname.html?fname=字符串乘法

## [224 基本计算器](https://leetcode-cn.com/problems/basic-calculator/)

左括号直接入栈

右括号，在弹出左括号前，清空运算

运算符号，清空运算，再入栈

空格和单元运算，可以通过替换字符串的方式，统一处理

参考：https://leetcode.cn/problems/basic-calculator/solution/shuang-zhan-jie-jue-tong-yong-biao-da-sh-olym/

## [227 基本计算器 II](https://leetcode-cn.com/problems/basic-calculator-ii/)

*本题运算符开始有优先级，故遇到运算符时需要考虑运算优先级，要是运算优先级比当前符号低，终止运算

参考：https://leetcode.cn/problems/basic-calculator-ii/solution/shi-yong-shuang-zhan-jie-jue-jiu-ji-biao-c65k/

## [772 基本计算器 III](https://leetcode-cn.com/problems/basic-calculator-iii/)

*同力扣227题，这题的测试用例有 -3//4 需要等于 0，而不是 -1,所以需要调整除法逻辑

参考：https://leetcode.cn/problems/basic-calculator-ii/solution/shi-yong-shuang-zhan-jie-jue-jiu-ji-biao-c65k/

## [42 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)

`res += min(l_max[i], r_max[i]) - height[i]`

参考：https://labuladong.github.io/article/fname.html?fname=接雨水

## [11 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)

`res = max(res, min(l_max, r_max) * (r - l))`

参考：https://labuladong.github.io/article/fname.html?fname=接雨水

## [20 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

左括号入栈，右括号匹配则出站，否则返回false，最后检查栈是否为空

> 左右各括号计数是不行的，因为括号有左右之分，比如][，计数就分辨不出

参考：https://labuladong.github.io/article/fname.html?fname=括号插入

## [921 使括号有效的最少添加](https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid/)

*遍历的过程中，有两种情况，左括号多了和右括号多了，可以以其中一项括号为基准，当它<0时，代表另一种括号多了，记录并回正（回正的意义在于不让二者的多余相抵），最后将两者相加即可

参考：https://labuladong.github.io/article/fname.html?fname=括号插入

## [1541 平衡括号字符串的最少插入次数](https://leetcode-cn.com/problems/minimum-insertions-to-balance-a-parentheses-string/)

*和力扣921题类似，不过这题的需要满足左括号前的右括号必须是双数

参考：https://labuladong.github.io/article/fname.html?fname=括号插入

## [391 完美矩形](https://leetcode-cn.com/problems/perfect-rectangle/)

只有四个顶点出现奇数次，这四个顶点围成面积和总和面积相等

> labuladong算法复杂在于用「最后四个顶点就应该构成完美矩形」这个特性来验证通过遍历得出的四个顶点，而不是直接验证总面积

参考：https://leetcode.com/problems/perfect-rectangle/discuss/1229993

## [855 考场就座](https://leetcode-cn.com/problems/exam-room/)

*坐和离开时维护连续空位们，坐时找到最长的连续空位，然后插入

参考：https://labuladong.github.io/article/fname.html?fname=座位调度

## [392 判断子序列](https://leetcode-cn.com/problems/is-subsequence/)

双指针

参考：https://labuladong.github.io/article/fname.html?fname=二分查找判定子序列

## [792 匹配子序列的单词数](https://leetcode-cn.com/problems/number-of-matching-subsequences/)

*char->char_indexs，然后遍历每个词的每个字母，二分查找

参考：https://labuladong.github.io/article/fname.html?fname=二分查找判定子序列

## [698 划分为k个相等的子集](https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/)

*剪枝

参考：https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/274942

## [78 子集](https://leetcode-cn.com/problems/subsets/)

### 二叉树遍历

所有元素，选与不选

参考：https://labuladong.github.io/article/fname.html?fname=子集排列组合

### 数学特性

`res += [x + [num] for x in res]`

参考：https://leetcode.com/problems/subsets/discuss/27301

## [77 组合](https://leetcode-cn.com/problems/combinations/)

同力扣78题，

求子集，不过是求长度为k的子集

参考：https://labuladong.github.io/article/fname.html?fname=子集排列组合
