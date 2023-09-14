'''
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
只使用数字1到9
每个数字 最多使用一次 
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

示例 1:
输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。

示例 2:
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。

示例 3:
输入: k = 4, n = 1
输出: []
解释: 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。

提示:
2 <= k <= 9
1 <= n <= 60
'''


### 方法一：选或不选
# 时间复杂度：O(k * C(9, k))
# 空间复杂度：O(k)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, path = [], []
        def dfs(i, tot):  # 当前数字为i，还需要的数字和为tot
            d = k - len(path)  # 还需要d个数
            if tot == 0 and d == 0:
                res.append(path.copy())  # 保存path
                return
            if i < d or tot < 0 or tot > (2 * i - d + 1) * d // 2:  # 剪枝
                return
            # 不选当前的数字
            dfs(i - 1, tot)
            # 选当前的数字
            path.append(i)
            dfs(i - 1, tot - i)
            path.pop()  # 恢复现场
        dfs(9, n)  # 倒序取数
        return res


### 方法二：枚举选项
# 时间复杂度：O(k * C(9, k))
# 空间复杂度：O(k)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, path = [], []
        def dfs(i, tot):  # 当前数字为i，还需要的数字和为tot
            d = k - len(path)  # 还需要d个数
            if tot == 0 and d == 0:
                res.append(path.copy())  # 保存path
                return
            if i < d or tot < 0 or tot > (2 * i - d + 1) * d // 2:  # 剪枝
                return
            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1, tot - j)
                path.pop()  # 恢复现场
        dfs(9, n)  # 倒序取数
        return res