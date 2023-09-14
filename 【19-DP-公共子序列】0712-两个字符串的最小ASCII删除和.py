'''
给定两个字符串 s1 和 s2，返回使两个字符串相等所需删除字符的 ASCII 值的最小和 。

示例 1:
输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。

示例 2:
输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。

提示:
0 <= s1.length, s2.length <= 1000
s1 和 s2 由小写英文字母组成
'''


'''
这是一个动态规划问题

状态定义：dp[i, j] 表示 s1[:i] 和 s2[:j] 的最小ASCII删除和。

分为4种情况：
1. s1[i] == s2[j]，此时等于 dp[i - 1, j - 1]
2. s1[i] != s2[j]，此时等于 min(dp[i - 1, j] + ord(s1[i]), dp[i, j - 1] + ord(s2[j]))

状态转移方程：如上述分类讨论
'''


### 方法一：记忆化搜索
# 时间复杂度：O(nm)
# 空间复杂度：O(nm)
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        @cache
        def dfs(i, j):
            if i < 0:
                return sum(ord(c) for c in s2[:j + 1])
            if j < 0:
                return sum(ord(c) for c in s1[:i + 1])
            if s1[i] == s2[j]:
                return dfs(i - 1, j - 1)
            return min(dfs(i - 1, j) + ord(s1[i]), dfs(i, j - 1) + ord(s2[j]))
        return dfs(n - 1, m - 1)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(nm)
# 空间复杂度：O(nm)
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0] = [0] + list(accumulate([ord(c) for c in s2]))
        for i in range(n):
            dp[i + 1][0] = dp[i][0] + ord(s1[i])
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1] + ord(s1[i]), dp[i + 1][j] + ord(s2[j]))
        return dp[n][m]
    

### 方法三：空间优化，两个数组
# 时间复杂度：O(nm)
# 空间复杂度：O(nm)
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(2)]
        dp[0] = [0] + list(accumulate([ord(c) for c in s2]))
        for i in range(n):
            dp[(i + 1) % 2][0] = dp[i % 2][0] + ord(s1[i])
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[(i + 1) % 2][j + 1] = dp[i % 2][j]
                else:
                    dp[(i + 1) % 2][j + 1] = min(dp[i % 2][j + 1] + ord(s1[i]), dp[(i + 1) % 2][j] + ord(s2[j]))
        return dp[n % 2][m]