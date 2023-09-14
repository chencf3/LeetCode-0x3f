'''
给你一个下标从 0 开始的 m x n 二进制矩阵 mat 和一个整数 cols ，表示你需要选出的列数。
如果一行中，所有的 1 都被你选中的列所覆盖，那么我们称这一行 被覆盖 了。
请你返回在选择 cols 列的情况下，被覆盖 的行数 最大 为多少。


示例 1：
输入：mat = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], cols = 2
输出：3
解释：
如上图所示，覆盖 3 行的一种可行办法是选择第 0 和第 2 列。
可以看出，不存在大于 3 行被覆盖的方案，所以我们返回 3 。

示例 2：
输入：mat = [[1],[0]], cols = 1
输出：2
解释：
选择唯一的一列，两行都被覆盖了，原因是整个矩阵都被覆盖了。
所以我们返回 2 。

提示：
m == mat.length
n == mat[i].length
1 <= m, n <= 12
mat[i][j] 要么是 0 要么是 1 。
1 <= cols <= n
'''


### 方法一：二进制枚举
# 时间复杂度：O(m * C(n, cols))
# 空间复杂度：O(m)
class Solution:
    def maximumRows(self, matrix: List[List[int]], cols: int) -> int:
        # 把每一行化为二进制集合表示
        mask = []
        for row in matrix:
            s = 0
            for j, v in enumerate(row):
                s += v << j  # 将二进制数 v 左移 j 位
            mask.append(s)
        res = 0
        for set in range(2 ** len(matrix[0])):  # 枚举所有可能的列
            if set.bit_count() == cols:  # 若二进制含1的个数恰好等于 cols
                tmp = 0
                for row in mask:  # 逐行判断是否覆盖该行所有1
                    if row & set == row:
                        tmp += 1
                res = max(res, tmp)
        return res