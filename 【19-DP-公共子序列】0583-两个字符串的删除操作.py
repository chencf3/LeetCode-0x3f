'''
给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
每步 可以删除任意一个字符串中的一个字符。

示例 1：
输入: word1 = "sea", word2 = "eat"
输出: 2
解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"

示例  2:
输入：word1 = "leetcode", word2 = "etco"
输出：4

提示：
1 <= word1.length, word2.length <= 500
word1 和 word2 只包含小写英文字母
'''


'''
这是一个动态规划问题

状态定义：dp[i, j] 表示 text1[:i] 和 text2[:j] 删除字符的最小步数。

分为3种情况：
1. text1[i] == text2[j]，此时等于 dp[i - 1, j - 1]
2. text1[i] != text2[j]，且在 text1 删除最后一个字母，此时等于 dp[i - 1, j] + 1
3. text1[i] != text2[j]，且在 text2 删除最后一个字母，此时等于 dp[i, j - 1] + 1

状态转移方程：如上述分类讨论
'''


### 方法一：记忆化搜索
# 时间复杂度：O(nm)
# 空间复杂度：O(nm)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        @cache
        def dfs(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if word1[i] == word2[j]:
                return dfs(i - 1, j - 1)
            return min(dfs(i - 1, j), dfs(i, j - 1)) + 1

        return dfs(n - 1, m - 1)


### 方法二：一比一翻译为递推
# 时间复杂度：O(nm)
# 空间复杂度：O(nm)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0] = [i for i in range(m + 1)]
        for i in range(n):
            dp[i + 1][0] = i + 1
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + 1
        return dp[n][m]
    

### 方法三：空间优化，两个数组
# 时间复杂度：O(nm)
# 空间复杂度：O(m)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(2)]
        dp[0] = [i for i in range(m + 1)]
        for i in range(n):
            dp[(i + 1) % 2][0] = i + 1
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[(i + 1) % 2][j + 1] = dp[i % 2][j]
                else:
                    dp[(i + 1) % 2][j + 1] = min(dp[i % 2][j + 1], dp[(i + 1) % 2][j]) + 1
        return dp[n % 2][m]


### 方法四：空间优化，一个数组
# 时间复杂度：O(nm)
# 空间复杂度：O(m)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = list(range(len(word2) + 1))
        for x in word1:
            pre = dp[0]
            dp[0] += 1
            for j, y in enumerate(word2):
                tmp = dp[j + 1]
                dp[j + 1] = pre if x == y else min(dp[j + 1], dp[j]) + 1
                pre = tmp
        return dp[-1]
    

### 方法五：利用最长公共子序列，直接用1143-最长公共子序列中的最优方法
# 时间复杂度：O(nm)
# 空间复杂度：O(m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for x in text1:
            pre = 0
            for j, y in enumerate(text2):
                tmp = dp[j + 1]
                dp[j + 1] = pre + 1 if x == y else max(dp[j + 1], dp[j])
                pre = tmp
        return dp[-1]
    
    def minDistance(self, word1: str, word2: str) -> int:
        return len(word1) + len(word2) - 2 * self.longestCommonSubsequence(word1, word2)