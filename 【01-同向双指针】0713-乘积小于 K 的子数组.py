'''
给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。

示例 1：
输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2]、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。

示例 2：
输入：nums = [1,2,3], k = 0
输出：0

提示: 
1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
'''


### 方法一：暴力枚举，超时
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(1)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        def product(i, j):
            prod = 1
            for k in range(i, j + 1):
                prod *= nums[k]
            return prod

        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if product(i, j) < k:
                    res += 1
                else:
                    break
        return res


### 方法二：同向双指针
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        mul, left = 1, 0
        for right, x in enumerate(nums):
            mul *= x
            while left <= right and mul >= k:
                mul //= nums[left]
                left += 1
            res += right - left + 1
        return res