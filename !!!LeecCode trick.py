# 排序
sorted(points, key=lambda x: x[0])
sorted(points, key=lambda x: [x[0], x[1]])


# 最大公约数
math.gcd(a, b)


### 1. 高阶函数 functools
(1) @cache  # 缓存装饰器，比带有大小限制的 lru_cache() 更小更快


### 2. 二分函数 bisect
from bisect import *
(1) bisect_left(a, x, lo=0, hi=len(a), *, key=None)
# 即第一个大于等于 x 的位置
'''
官方解释：在 a 中找到 x 合适的插入点以维持有序。参数 lo 和 hi 可以被用于确定需要考虑的子集；默认情况下整个列表都会被使用。如果 x 已经在 a 里存在，那么插入点会在已存在元素之前（也就是左边）。如果 x 大于 a 中的所有值，就放在最后。
'''
(2) bisect_right(a, x, lo=0, hi=len(a), *, key=None)
# 即第一个大于 x 的位置
(3) insort_left(a, x, lo=0, hi=len(a), *, key=None)
(4) insort_right(a, x, lo=0, hi=len(a), *, key=None)


### 3. 迭代器 itertools
from itertools import *
(1) accumulate()  # 累加器
list(accumulate([1, 2, 3, 4]))
[1, 3, 6, 10]
(2) pairwise()  # 返回长度为2的所有子串
pairwise('12345')
12 23 34 45
(3) product()  # 返回笛卡尔积
product('ABCD', 'ABCD')
AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
(4) permutations()  # 返回无重复元素的长度为r的排列
permutations('ABCD', 2)
AB AC AD BA BC BD CA CB CD DA DB DC
(5) combinations()  # 返回无重复元素的长度为r的子序列
combinations('ABCD', 2)
AB AC AD BC BD CD
(6) combinations_with_replacement()  # 返回有重复元素的长度为r的有序组合
combinations_with_replacement('ABCD', 2)
AA AB AC AD BB BC BD CC CD DD


### 4. 最小堆 heapq
import heapq
其中 heap 是堆名
(1) heapq.heapify(x)  # 将list x 转换成堆，原地，线性时间内
(2) heapq.heappush(heap, item)  # 将 item 的值加入 heap 中，保持堆的不变性
(3) heapq.heappop(heap)  # 弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出IndexError。使用 heap[0] ，可以只访问最小的元素而不弹出它
(4) heapq.heappushpop(heap, item)  # 将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用 heappush() 再调用 heappop() 运行起来更有效率
(5) heapq.heapreplace(heap, item)  # 弹出并返回 heap 中最小的一项，同时推入新的 item。堆的大小不变。如果堆为空则引发IndexError。这个单步骤操作比 heappop() 加 heappush() 更高效，并且在使用固定大小的堆时更为适宜
(6) heapq.nlargest(n, iterable, key=None)  # 从 iterable 所定义的数据集中返回前 n 个最大元素组成的已按从大到小排序的列表
(7) heapq.nsmallest(n, iterable, key=None)  # 从 iterable 所定义的数据集中返回前 n 个最小元素组成的已按从小到大排序的列表


### 5. 容器数据类型 collections
from collections import *
(1) Counter()  # 计数器
# most_common(n)  # 返回一个列表，其中包含 n 个最常见的元素及出现次数，按常见程度由高到低排序
(2) deque()  # 双端队列
# append(x)  # 添加 x 到右端
# appendleft(x)  # 添加 x 到左端
# clear()  # 移除所有元素，使其长度为0
# count(x)  # 计算 deque 中元素等于 x 的个数
# index(x[, start[, stop]])  # 返回 x 在 deque 中的位置（在索引 start 之后，索引 stop 之前）。 返回第一个匹配项，如果未找到则引发 ValueError
# insert(i, x)  # 在位置 i 插入 x
# pop()  # 移去并且返回一个元素，deque 最右侧的那一个。 如果没有元素的话，就引发 IndexError
# popleft()  # 移去并且返回一个元素，deque 最左侧的那一个。 如果没有元素的话，就引发 IndexError
# remove(value)  # 移除找到的第一个 value。 如果没有的话就引发 ValueError
# reverse()  # 将 deque 逆序排列。返回 None
# rotate(n=1)  # 向右循环移动 n 步。如果 n 是负数，就向左循环。如果 deque 不是空的，向右循环移动一步就等价于 d.appendleft(d.pop())，向左循环一步就等价于 d.append(d.popleft())
(3) defaultdict()  # 初始化字典，指定值的类型
defaultdict(default_factory=None)
# defaultdict(list)
# defaultdict(int)