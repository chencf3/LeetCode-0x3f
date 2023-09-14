'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1

提示：
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4

进阶：
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
'''


'''
这是一个动态规划问题

状态定义：dp[i] 表示以 nums[i] 为结尾的最长递增子序列长度

状态转移方程：dp[i] = max(dp[j]) + 1，其中 j < i 且 nums[j] < nums[i]
'''


### 方法一：记忆化搜索
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1

        return max(dfs(i) for i in range(n))


### 方法二：一比一翻译为递推
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dp[j])
            dp[i] = res + 1
        return max(dp)
    

### 方法三：利用原数组、原数组的严格递增数组求最长公共子序列，实际运行很慢
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n)
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
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        text2 = sorted(set(nums))
        return self.longestCommonSubsequence(nums, text2)


### 方法四：贪心 + 二分查找，有额外空间
# 时间复杂度：O(n log n)
# 空间复杂度：O(n)
'''
g 数组中：g[i] 表示长度为 i + 1 的最长递增子序列的末尾元素的最小值
g 数组严格递增
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []
        for num in nums:
            i = bisect_left(g, num)
            if i == len(g):  # 在 g 的末尾添加元素
                g.append(num)
            else:  # 修改元素
                g[i] = num
        return len(g)
    

### 方法五：贪心 + 二分查找，原地修改
# 时间复杂度：O(n log n)
# 空间复杂度：O(1)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ng = 0  # g 的长度
        for num in nums:
            i = bisect_left(nums, num, 0, ng)  # 在 nums[0:ng] 之间寻找第一个大于等于 x 的位置
            nums[i] = num
            if i == ng:
                ng += 1
        return ng