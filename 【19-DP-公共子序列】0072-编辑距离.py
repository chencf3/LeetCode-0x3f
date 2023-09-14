'''
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

提示：
0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成
'''


'''
这是一个动态规划问题

状态定义：dp[i, j] 表示 text1[:i] 和 text2[:j] 的编辑距离。

分为4种情况：
1. text1[i] == text2[j]，此时等于 dp[i - 1, j - 1]
2. text1[i] != text2[j]，且在 text1 的最后新增一个字母，用于跟 text2 的最后一个字母相等，此时等于 dp[i, j - 1] + 1
3. text1[i] != text2[j]，且在 text1 的最后删除一个字母，此时等于 dp[i - 1, j] + 1
4. text1[i] != text2[j]，且在 text1 的最后修改一个字母，用于跟 text2 的最后一个字母相等，此时等于 dp[i - 1, j - 1] + 1

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
            return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1

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
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
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
                    dp[(i + 1) % 2][j + 1] = min(dp[i % 2][j + 1], dp[(i + 1) % 2][j], dp[i % 2][j]) + 1
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
                dp[j + 1] = pre if x == y else min(pre, dp[j + 1], dp[j]) + 1
                pre = tmp
        return dp[-1]