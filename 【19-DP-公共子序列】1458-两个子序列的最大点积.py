'''
给你两个数组 nums1 和 nums2 。
请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。
数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。比方说，[2,3,5] 是 [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。

示例 1：
输入：nums1 = [2,1,-2,5], nums2 = [3,0,-6]
输出：18
解释：从 nums1 中得到子序列 [2,-2] ，从 nums2 中得到子序列 [3,-6] 。
它们的点积为 (2*3 + (-2)*(-6)) = 18 。

示例 2：
输入：nums1 = [3,-2], nums2 = [2,-6,7]
输出：21
解释：从 nums1 中得到子序列 [3] ，从 nums2 中得到子序列 [7] 。
它们的点积为 (3*7) = 21 。

示例 3：
输入：nums1 = [-1,-1], nums2 = [1,1]
输出：-1
解释：从 nums1 中得到子序列 [-1] ，从 nums2 中得到子序列 [1] 。
它们的点积为 -1 。

提示：
1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 100
'''


'''
这是一个动态规划问题

状态定义：dp[i, j] 表示 nums1[:i] 和 nums2[:j] 的最大点积。

分为4种情况：
1. 选 nums1[i] * nums2[j]，且继续考虑 dp[i - 1, j - 1]，此时等于 dp[i - 1, j - 1] + nums1[i] * nums2[j]
2. 选 nums1[i] * nums2[j]，且不考虑 dp[i - 1, j - 1]，此时等于 nums1[i] * nums2[j]
3. 不选 nums1[i]，此时等于 dp[i - 1, j]
4. 不选 nums2[i]，此时等于 dp[i, j - 1]

状态转移方程：取上述4种情况的最大值
'''


### 方法一：记忆化搜索
# 时间复杂度：O(nm)
# 空间复杂度：O(nm)
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return -inf
            return max(nums1[i] * nums2[j], nums1[i] * nums2[j] + dfs(i - 1, j - 1), dfs(i - 1, j), dfs(i, j - 1))

        return dfs(n - 1, m - 1)
    

### 方法二：一比一翻译为递推
# 时间复杂度：O(nm)
# 空间复杂度：O(nm)
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[-inf] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                dp[i + 1][j + 1] = max(x * y, x * y + dp[i][j], dp[i][j + 1], dp[i + 1][j])
        return dp[n][m]
    

### 方法三：空间优化，两个数组
# 时间复杂度：O(nm)
# 空间复杂度：O(m)
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[-inf] * (m + 1) for _ in range(2)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                dp[(i + 1) % 2][j + 1] = max(x * y, x * y + dp[i % 2][j], dp[i % 2][j + 1], dp[(i + 1) % 2][j])
        return dp[n % 2][m]