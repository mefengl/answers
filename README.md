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

k个元素的组合是子集树的k层节点

> len(val)决定层数，而不是num(idx+1)，那只是选择

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

## [19 删除链表的倒数第N个节点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) 

双指针构成一条定长绳

参考：https://labuladong.github.io/article/fname.html?fname=链表技巧

## [876 中间值](https://leetcode.cn/problems/middle-of-the-linked-list/) 

一步两步

参考：https://labuladong.github.io/article/fname.html?fname=链表技巧

## [160 两个链表的第一个公共节点](https://leetcode.cn/problems/intersection-of-two-linked-lists/) 

a+b=b+a

## [76 最小路径和](https://leetcode.cn/problems/minimum-ascent-path/) 

right可行解，left局部最优解

参考：https://labuladong.github.io/article/fname.html?fname=滑动窗口技巧进阶

## [567 字符串的排列](https://leetcode.cn/problems/permutation-in-string/) 

True: 长度和valid

参考：https://labuladong.github.io/article/fname.html?fname=滑动窗口技巧进阶

## [3 最长无重复字符的子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) 

不需要need的滑动窗口

参考：https://labuladong.github.io/article/fname.html?fname=滑动窗口技巧进阶

## [206 链表反转](https://leetcode.cn/problems/reverse-linked-list/) 

last = self.reverseList(head.next)

参考：https://labuladong.github.io/article/fname.html?fname=递归反转链表的一部分

## [92 链表反转 II](https://leetcode.cn/problems/reverse-linked-list-ii/) 

successor相当与链表全反最后的null，调到开始处，反转前k个

参考：https://labuladong.github.io/article/fname.html?fname=递归反转链表的一部分

## [25 反转链表中的每个组](https://leetcode.cn/problems/reverse-nodes-in-k-group/) 

不停地反转前k个

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

> 每次遍历前的if也太不优雅了，但一时间内没有想到更好的解法

参考：https://labuladong.github.io/article/fname.html?fname=花式遍历

## [99 恢复二叉搜索树](https://leetcode.cn/problems/recover-binary-search-tree/) 

中序遍历得到仅一对错误的有序数组，通过双指针恢复

参考：插件内labuladong思路

## [124 二叉树的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) 

和二叉树宽度类似，但需要将小于0的路径置为0

参考：插件内labuladong思路

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

和105一样，小窍门是：inorder和postorder的长度永远是相同的，可以按照它推断索引范围

参考：各序遍历规律

## [889 根据前序和后序遍历构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) 

之所以需要中序遍历，是为了确认前序遍历里的第二个元素是左节点还是右节点（当左数长度为0时是右节点），此题两种情况都可以

参考：https://labuladong.github.io/article/fname.html?fname=二叉树系列2

## [297 序列化二叉树](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) 

前序后序均可，因为可用特殊符号表示空节点，后序解析时先右树后左树

参考：https://labuladong.github.io/article/fname.html?fname=二叉树的序列化

## [652 检测重复的子树](https://leetcode.cn/problems/find-duplicate-subtrees/) 

核心是297序列化二叉树，此外就是判断是否已出现且仅出现一次

参考：https://labuladong.github.io/article/fname.html?fname=二叉树系列3

## [912 排序数组](https://leetcode.cn/problems/sort-an-array/) 

### 归并排序
*在后序归并前面已经排好序的数组

参考：https://labuladong.github.io/article/fname.html?fname=归并排序

### 快速排序
在前序将每个元素放在正确的序号位置上

参考：https://labuladong.github.io/article/fname.html?fname=快速排序

## [315 计算右侧小于当前元素的个数](https://leetcode.cn/problems/count-of-smaller-numbers-after-self/) 

在每次归并中，前指针和mid之间的元素便是「右侧小于当前元素的个数」

参考：https://labuladong.github.io/article/fname.html?fname=归并排序

## [493 翻转对](https://leetcode.cn/problems/reverse-pairs/) 

*比力扣315需要的技巧还少些，利用merge的同子树只比较一次和合并的两个数组各自是有序的两个特性去做，利用归并排序merge中数组有序得到范围解（因为右子树有序，如果end比左子树某元素两倍还小，则从mid+1到end都是解，这样end-(mid+1)便为解的个数）

参考：https://labuladong.github.io/article/fname.html?fname=归并排序

## [327 计算区间和的个数](https://leetcode.cn/problems/count-of-range-sum/) 

前缀和用来快速计算区间和，利用归并排序merge中数组有序可以得到范围解（因为右子树有序，根据前缀和的计算方式，在减数不变的情况下，对应的区间和也是有序的，通过start排除，通过end收纳，则从start到end都是解，这样end-start便为解的个数）

参考：https://labuladong.github.io/article/fname.html?fname=归并排序

## [230 求二叉搜索树的第k小元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/) 

二叉搜索树 中序遍历 升序进行

参考：https://labuladong.github.io/article/fname.html?fname=BST1

## [538 将二叉搜索树转换为累加树](https://leetcode.cn/problems/convert-bst-to-greater-tree/) 

二叉搜索树 中序遍历 先右后左 降序进行，维持累加变量并赋值即可

> 二叉搜索树的中序遍历问题往往是有序数组问题

参考：https://labuladong.github.io/article/fname.html?fname=BST1

## [1038 将二叉搜索树转换为累加树](https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/) 

同力扣538，二叉搜索树 中序遍历 先右后左 降序进行，维持累加变量并赋值即可

> 二叉搜索树的中序遍历问题往往是有序数组问题

参考：https://labuladong.github.io/article/fname.html?fname=BST1

## [98 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/) 

通过参数，将root的约束传递到子孙节点

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

*左和右子树的组合笛卡尔乘积就是根节点的所有组合

参考：https://labuladong.github.io/article/fname.html?fname=BST3

##[215 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)

快速排序的partition函数，在这里可以起到二分查找里结果函数的作用（ 类似nums[mid]，这里是partition(nums,lo,hi) ）

> 数组可以获得长度，所以第K大可以转化成别的东西

## [341 扁平化嵌套列表迭代器](https://leetcode.cn/problems/flatten-nested-list-iterator/)

将头部的非整数变成整数放回去

## [236 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)

两种情况，一种是其中节点就是要找的元素（它本身就是祖先），另一种是节点左右子树都能找到对应元素，这也是祖先（因为需要左右遍历完成，所以后序）

## [1676 二叉树的最近公共祖先-iv](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iv)

> 同力扣236题，两种情况，一种是其中节点就是要找的元素（它本身就是祖先），另一种是节点左右子树都能找到对应元素，这也是祖先（因为需要左右遍历完成，所以后序）。

和第一种情况就能直接判断祖先元素一样，不需要所有元素都找到，因为二叉树遍历特点，剩下的元素必然在没有遍历的子树里。

## [1644 二叉树的最近公共祖先-ii](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-ii/)

> 类似力扣236与1676题

这题的特点是，节点不一定存在，所以无论如何整颗树要遍历完成，所以后序遍历（仍然要及时返回找到的节点，但这里的找到无法决定是否有祖先节点，得根据全局的flag判断）

## [235 二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)

由搜索二叉树性质，`p.val <= root.val <= q.val` ，则root就是最近公共祖先

## [1650 二叉树的最近公共祖先-iii](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iii/)

类似力扣160题，本质是求 两条链表交点

## [222 完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/)

暴力：纯遍历，计算节点个数；
满二叉树：2**n - 1；
完全二叉树：子树是满二叉树（左右高度相同）用满二叉树，子树是普通树（左右高度不同）用纯遍历

## [797 所有可能的路径](https://leetcode.cn/problems/all-paths-from-source-to-target/)

图的遍历等同于多叉树遍历，但需要加上visited数组防重复访问，如果需要记录路径，则需要维护路径数组

## [207 课程表](https://leetcode.cn/problems/course-schedule/)

### DFS
从所有节点出发一次，看是否会路径这条蛇是否会咬到自己，咬到代表成环，代表不可能学完

### BFS
不成环的图，从入度为0的节点一个个消除，可以消除殆尽

## [210 课程表 II](https://leetcode.cn/problems/course-schedule-ii/)

### DFS
beg->[end]的树结构，后序遍历能保证beg们已经访问过了，最后结果需要reverse

### BFS
消除（popleft）的顺序就是拓扑排序的顺序

## [785 判断二分图](https://leetcode.cn/problems/is-graph-bipartite/) 

### DFS
遍历所有子树，没访问过的节点赋反色，访问过的节点检查是否为反色

### BFS
和DFS几乎相同，但通过队列来遍历

## [886 可能得二分法](https://leetcode.cn/problems/possible-bipartition/)

和力扣785相同，是一个判断二分图的问题，需要将相互讨厌关系转化为图结构

## [323 无向图中连通分量的数目](https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/)

并查集算法，连通分量最大数目是每个节点都是一个子树（通过根节点区分），通过UNION函数遍历题目给的边，如果边的两个节点都是一个子树（通过FIND找到根节点判别），则不变，如果不是，则将两个节点合并为一个子树（同一个根节点），连通分量减一

参考：https://labuladong.github.io/article/fname.html?fname=UnionFind算法详解

## [130 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)

并查集可以解决，用神圣的dummy连接所有BIG_O，最后没和dummy连接的是BIG_X

参考：https://labuladong.github.io/article/fname.html?fname=UnionFind算法详解

## [990 等式方程的可满足性](https://leetcode.cn/problems/satisfiability-of-equality-equations/)

遍历，如果==，则两个节点必须在一个子树中，连接；
遍历，如果!=，则两个节点必须在不同的子树中（非is_connected），否则，返回False

参考：https://labuladong.github.io/article/fname.html?fname=UnionFind算法详解

## [261 以图判树](https://leetcode.cn/problems/graph-valid-tree/)

并查集可以解决，连接所有的边，连接之前，两条边不允许连通，否则返回False，最后，如果只生成一颗子树（uf.count == 1）返回True

参考：https://labuladong.github.io/article/fname.html?fname=kruskal

## [1135 最低成本联通所有城市](https://leetcode.cn/problems/connecting-cities-with-minimum-cost/)

### Kruskal

并查集可以解决，核心是将connections按cost排序，然后逐次连接并更新cost，连接过的跳过（不然成环，不是树），最后，如果只生成一颗子树（uf.count == 1）返回True

参考：https://labuladong.github.io/article/fname.html?fname=kruskal

### Prim

从0开始，不断切割最短边（优先队列），并切割对应节点（钝刀子），如果最后所有节点都cut过，返回True，否则返回False

参考：https://labuladong.github.io/article/fname.html?fname=prim算法

## [1584 连接所有点的最小费用](https://leetcode.cn/problems/connecting-cities-with-minimum-cost/)

### Kruskal

并查集可以解决，核心是将points转换成带cost的edges，然后逐次连接并更新cost，连接过的跳过（不然成环，不是树），最后，如果只生成一颗子树（uf.count == 1）返回True（这一题只会有一个子树）

参考：https://labuladong.github.io/article/fname.html?fname=kruskal

### Prim

基本的Prim算法，除此之外，核心是build_graph，从0开始，不断切割最短边（优先队列），并切割对应节点（钝刀子），如果最后所有节点都cut过（此题一定全cut），返回True，否则返回False

参考：https://labuladong.github.io/article/fname.html?fname=prim算法

## [743 网络延迟时间](https://leetcode.cn/problems/network-delay-time/)

*Dijkstra算法，先建立graph，然后层序遍历，如果不是更小，就跳过

参考：https://labuladong.github.io/article/fname.html?fname=dijkstra算法

## [1631 最小体力消耗路径](https://leetcode.cn/problems/minimum-energy-cost-to-make-walkable-road/)

Dijkstra算法，先建立graph，然后层序遍历，如果不是更小，就跳过。特殊地方在于，一条路径的最大消耗由每一步的最大值而不是总和决定

参考：https://labuladong.github.io/article/fname.html?fname=dijkstra算法

## [1514 概率最大的路径](https://leetcode.cn/problems/path-with-maximum-probability/)

Dijkstra算法，不过是求最大，所以相应的判断需要取反，另外优先队列需要逆序（压入时加负号，取出时回正也是一个方法）

参考：https://labuladong.github.io/article/fname.html?fname=dijkstra算法

## [277 搜寻名人](https://leetcode.cn/problems/find-the-celebrity/)

擂台制，如果candidate认识other或者other不认识candidate，candidate都不可能是名人。最后，candidate还要和所有人再比一把（防止石头剪刀布式的胜利）

参考：https://labuladong.github.io/article/fname.html?fname=名人问题

## [146 LRU 缓存](https://leetcode.cn/problems/lru-cache/)

*双向链表+hashmap。LRU算法要求，双向链表需要实现尾部增，头部删，各处删的方法；另外，需要根据get和put函数的情况，在中间封装一批函数（总之多做，是有逻辑的）

参考：https://labuladong.github.io/article/fname.html?fname=LRU算法

## [460 LFU 缓存](https://leetcode.cn/problems/lfu-cache/)

*对key_to_val/freq、freq_to_keys，还有min_freq的同步更新

参考：https://labuladong.github.io/article/fname.html?fname=LFU

## [292 Nim 游戏](https://leetcode.cn/problems/nim-game/)

永远不能是4的倍数

参考：labuladong的算法小抄 5.13.1

## [877 石子游戏](https://leetcode.cn/problems/stone-game/)

先手预定奇数或偶数堆，鉴于共偶数堆且奇数个，先手必赢

参考：labuladong的算法小抄 5.13.2

## [319 灯泡开关](https://leetcode.cn/problems/bulb-switcher/)

因子问题，亮着的灯泡需要具有两个相同因子，即平方数；故本题为统计n前的平方数问题，sqrt后转int即可

参考：labuladong的算法小抄 5.13.3

## [208 实现Trie](https://leetcode.cn/problems/implement-trie-prefix-tree/)

前缀树，可以理解为嵌套的字典结构，键为字符，值为字典，如果是叶子节点，值为true，否则为字典

参考：https://leetcode.com/problems/implement-trie-prefix-tree/discuss/362916

## [191 位1的个数](https://leetcode.cn/problems/number-of-1-bits/)

n&(n-1)，每次去掉最低位1，直到n为0，统计的次数即为1的个数

参考：https://labuladong.github.io/article/fname.html?fname=常用的位操作

## [231 2的幂](https://leetcode.cn/problems/power-of-two/)

2的幂，只有一个1，必为最低位，所以去掉最低位1，一定为0，即n&(n-1)==0

参考：https://labuladong.github.io/article/fname.html?fname=常用的位操作

## [136 只出现一次的数字](https://leetcode.cn/problems/single-number/)

> 一个数和它本身做异或运算结果为 0，即 a ^ a = 0；一个数和 0 做异或运算的结果为它本身，即 a ^ 0 = a。

全部异或后，最后一个数即为唯一的数

参考：https://labuladong.github.io/article/fname.html?fname=常用的位操作

## [268 丢失的数字](https://leetcode.cn/problems/missing-number/)

> 一个数和它本身做异或运算结果为 0，即 a ^ a = 0；一个数和 0 做异或运算的结果为它本身，即 a ^ 0 = a。

原有数组和[0-n]数组异或，最后一个数即为唯一的数（注意0-n有n+1个数）

参考：https://labuladong.github.io/article/fname.html?fname=常用的位操作

## [172 阶乘后的零](https://leetcode.cn/problems/factorial-trailing-zeroes/)

寻找有几对具有2因子的因子和具有5因子的因子，因为2的因子一定比5的因子多，所以只需要求出5的因子个数即可，自除5的和即为结果

参考：https://labuladong.github.io/article/fname.html?fname=阶乘题目

## [793 阶乘函数后]

由力扣172题，已知求阶乘尾部0个数的方法，该方法可以作为二分法的核心函数，求出左右边界，左右边界中的元素个数即为所求
