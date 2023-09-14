'''
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [nums[l], nums[l+1], ..., nums[r-1], nums[r]] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：
输入：target = 4, nums = [1,4,4]
输出：1

示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

提示：
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

进阶：
如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
'''


### 方法一：暴力枚举，超时
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = inf
        for i in range(n):
            for j in range(i, n):
                if sum(nums[i: j + 1]) >= target:
                    res = min(res, j - i + 1)
                    break
        return res if res != inf else 0


### 方法二：前缀和 + 二分
# 时间复杂度：O(n log n)
# 空间复杂度：O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        presum = [0] + list(accumulate(nums))
        res = inf
        for i in range(n + 1):
            j = bisect_left(presum, target + presum[i])
            if j != n + 1:
                res = min(res, j - i)
        return res if res != inf else 0


### 方法三：同向双指针
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = inf
        tot, left = 0, 0
        for right, x in enumerate(nums):
            tot += x
            while tot >= target:
                res = min(res, right - left + 1)
                tot -= nums[left]
                left += 1
        return res if res != inf else 0