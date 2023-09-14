'''
给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
注意：不允许旋转信封。

示例 1：
输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

示例 2：
输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1

提示：
1 <= envelopes.length <= 10^5
envelopes[i].length == 2
1 <= wi, hi <= 10^5
'''


'''
必须要保证对于每一种 w 值，最多只能选择 1 个信封。可以将 h 值作为排序的第二关键字进行降序排序，这样一来，对于每一种 w 值，其对应的信封在排序后的数组中是按照 h 值递减的顺序出现的，那么这些 h 值不可能组成长度超过 1 的严格递增的序列，这就从根本上杜绝了错误的出现。
'''


### 方法一：贪心 + 二分查找
# 时间复杂度：O(n log n)
# 空间复杂度：O(n)
'''
g 数组中：g[i] 表示长度为 i + 1 的最长递增子序列的末尾元素的最小值
g 数组严格递增
'''
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        envelopes.sort(key=lambda x: [x[0], -x[1]])
        g = []
        for _, height in envelopes:
            j = bisect_left(g, height)
            if j == len(g):  # 在 g 的末尾添加元素
                g.append(height)
            else:  # 修改元素
                g[j] = height
        return len(g)