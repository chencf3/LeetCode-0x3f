'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 2：
输入：s = "a"
输出：[["a"]]

提示：
1 <= s.length <= 16
s 仅由小写英文字母组成
'''


### 方法一：选或不选，定义回溯时用两个变量
# 时间复杂度：O(n * 2 ^ n)
# 空间复杂度：O(n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        n = len(s)
        def dfs(i, j):  # i表示当前子串开始位置，j表示当前指针位置
            if j == n:  # 终止条件
                res.append(path.copy())  # 保存path
                return
            # 不选第j个字母之后的逗号
            if j < n - 1:
                dfs(i, j + 1)
            # 选第i个字母之后的逗号
            t = s[i: j + 1]
            if t == t[::-1]:
                path.append(t)
                dfs(j + 1, j + 1)
                path.pop()  # 恢复现场
        dfs(0, 0)
        return res


### 方法二：选或不选
# 时间复杂度：O(n * 2 ^ n)
# 空间复杂度：O(n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        n = len(s)

        def dfs(i, t):
            if i == n:
                if ''.join(path) == s:
                    res.append(path.copy())
                return
            t += s[i]
            dfs(i + 1, t)  # 不选
            if t == t[::-1]:
                path.append(t)
                dfs(i + 1, '')  # 选
                path.pop()

        dfs(0, '')
        return res


### 方法三：枚举选项，即枚举子串的结束位置
# 时间复杂度：O(n * 2 ^ n)
# 空间复杂度：O(n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        n = len(s)
        def dfs(i):  # i表示当前子串开始位置
            if i == n:  # 终止条件
                res.append(path.copy())  # 保存path
                return
            for j in range(i, n):  # 枚举子串的结束位置
                t = s[i: j + 1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()  # 恢复现场
        dfs(0)
        return res