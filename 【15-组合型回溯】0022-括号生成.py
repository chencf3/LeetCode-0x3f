'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

提示：
1 <= n <= 8
'''


### 方法一：枚举此时选左括号还是右括号
# 时间复杂度：O(n * C(2n, n))，即在 2n 个位置中选 n 个位置放左括号
# 空间复杂度：O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []

        def dfs(left, right):
            if left == n and right == n:  # 终止条件
                res.append(''.join(path))
                return
            if left < n:  # 如果左括号个数小于 n，还可以选左括号
                path.append('(')
                dfs(left + 1, right)
                path.pop()
            if left > right:  # 如果左括号个数大于右括号个数，还可以选右括号
                path.append(')')
                dfs(left, right + 1)
                path.pop()

        dfs(0, 0)
        return res
    

### 方法二：枚举此时选左括号还是右括号
# 时间复杂度：O(n * C(2n, n))，即在 2n 个位置中选 n 个位置放左括号
# 空间复杂度：O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []
        def dfs(i):
            if len(path) == 2 * n:
                res.append(''.join(path))
                return
            cnt = path.count('(')
            if cnt < n:  # 如果左括号个数小于 n，还可以选左括号
                path.append('(')
                dfs(i + 1)
                path.pop()
            if cnt > i - cnt:  # 如果左括号个数大于右括号个数，还可以选右括号
                path.append(')')
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res