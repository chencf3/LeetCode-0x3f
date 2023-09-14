'''
给你两个字符串 word1 和 word2 ，请你按下述方法构造一个字符串：
从 word1 中选出某个 非空 子序列 subsequence1 。
从 word2 中选出某个 非空 子序列 subsequence2 。
连接两个子序列 subsequence1 + subsequence2 ，得到字符串。
返回可按上述方法构造的最长 回文串 的 长度 。如果无法构造回文串，返回 0 。
字符串 s 的一个 子序列 是通过从 s 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。
回文串 是正着读和反着读结果一致的字符串。

示例 1：
输入：word1 = "cacb", word2 = "cbba"
输出：5
解释：从 word1 中选出 "ab" ，从 word2 中选出 "cba" ，得到回文串 "abcba" 。

示例 2：
输入：word1 = "ab", word2 = "ab"
输出：3
解释：从 word1 中选出 "ab" ，从 word2 中选出 "a" ，得到回文串 "aba" 。

示例 3：
输入：word1 = "aa", word2 = "bb"
输出：0
解释：无法按题面所述方法构造回文串，所以返回 0 。

提示：
1 <= word1.length, word2.length <= 1000
word1 和 word2 由小写英文字母组成
'''


'''
这是一个动态规划问题

状态定义：dp[i, j] 表示使 s[i] 到 s[j] 为回文串的最少插入次数

分为2种情况：
1. 若s[i] == s[j]，此时 dp[i, j] = dp[i + 1, j - 1]
2. 若s[i] != s[j]，此时 dp[i, j] = min(dp[i + 1, j], dp[i, j - 1]) + 1

状态转移方程：如上述分类讨论

边界条件：
dp[i, i] = 1
dp[i, j] = 0，其中 i > j
'''


### 方法一：记忆化搜索
# 时间复杂度：O((n + m) ^ 2)
# 空间复杂度：O((n + m) ^ 2)
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n, m = len(word1), len(word2)
        @cache
        def dfs(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            elif s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2
            return max(dfs(i, j - 1), dfs(i + 1, j))
            
        res = 0
        for h in range(m - 1, -1, -1):
            if word2[h] in word1:
                res = max(res, dfs(word1.find(word2[h]), n + h))
        return res
    

### 方法二：递推
# 时间复杂度：O((n + m) ^ 2)
# 空间复杂度：O((n + m) ^ 2)
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        res = 0
        s = word1 + word2
        n, m = len(word1), len(word2)
        dp = [[0] * (n + m) for _ in range(n + m)]
        for i in range(n + m - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n + m):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if i < n <= j:  # 满足此条件时才更新答案
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return res