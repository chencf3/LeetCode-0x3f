'''
给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
请你返回让 s 成为回文串的 最少操作次数 。
「回文串」是正读和反读都相同的字符串。

示例 1：
输入：s = "zzazz"
输出：0
解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。

示例 2：
输入：s = "mbadm"
输出：2
解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。

示例 3：
输入：s = "leetcode"
输出：5
解释：插入 5 个字符后字符串变为 "leetcodocteel" 。

提示：
1 <= s.length <= 500
s 中所有字符都是小写字母。
'''


'''
这是一个动态规划问题

状态定义：dp[i, j] 表示使 s[i] 到 s[j] 为回文串的最少插入次数

分为2种情况：
1. 若s[i] == s[j]，此时 dp[i, j] = dp[i + 1, j - 1]
2. 若s[i] != s[j]，此时 dp[i, j] = min(dp[i + 1, j], dp[i, j - 1]) + 1

状态转移方程：如上述分类讨论

边界条件：
dp[i, i] = 0
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n ^ 2)
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            return min(dfs(i, j - 1), dfs(i + 1, j)) + 1
        return dfs(0, n - 1)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n ^ 2)
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i >= j:  # 已初始化为0，因此可以 pass
                    pass
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
        return dp[0][n - 1]
    

### 方法三：字符串长度 - 最长回文子序列长度
# 采用0516-最长回文子序列的最优解法
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n)
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            pre = 0
            for j in range(i + 1, n):
                tmp = dp[j]
                dp[j] = pre + 2 if s[i] == s[j] else max(dp[j], dp[j - 1])
                pre = tmp
        return n - dp[-1]