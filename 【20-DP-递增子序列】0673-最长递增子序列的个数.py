'''
给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。
注意 这个数列必须是 严格 递增的。

示例 1:
输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

示例 2:
输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。

提示: 
1 <= nums.length <= 2000
-10^6 <= nums[i] <= 10^6
'''


'''
这是一个动态规划问题

状态定义：
dp[i] 表示以 nums[i] 为结尾的最长递增子序列长度
cnt[i] 表示以 nums[i] 为结尾的最长递增子序列个数

状态转移方程：
dp[i] = max(dp[j]) + 1，其中 j < i 且 nums[j] < nums[i]
'''


### 方法一：递推
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # 以 nums[i] 结尾的最长递增子序列的长度
        cnt = [1] * n  # 以 nums[i] 结尾的最长递增子序列的个数
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] == dp[j] + 1:  # 之前已遇到过最长子序列
                        cnt[i] += cnt[j]
                    elif dp[i] < dp[j] + 1:  # 需要更新最长子序列
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
        mx = max(dp)
        return sum(cnt[i] for i in range(n) if dp[i] == mx)