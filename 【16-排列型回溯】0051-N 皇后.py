'''
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]

提示：
1 <= n <= 9
'''


### 方法一：回溯
# 时间复杂度：O(n!)
# 空间复杂度：O(n)
'''
问题可转化为从 1 到 n 中全排列
path的第 i 个数为 x，表示第 i 行第 j 列有一个皇后
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, path = [], []

        def check(c, path):
            m = len(path)
            for i, x in enumerate(path):
                if abs(m - i) == abs(c - x):
                    return False
            return True

        def dfs(i, unvisited):
            if i == n:
                res.append(['.' * path[row] + 'Q' + '.' * (n - 1 - path[row]) for row in range(n)])
                return
            for c in unvisited:
                if check(c, path):
                    path.append(c)
                    dfs(i + 1, unvisited - {c})
                    path.pop()

        dfs(0, set([i for i in range(n)]))
        return res