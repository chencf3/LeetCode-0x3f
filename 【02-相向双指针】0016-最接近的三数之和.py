'''
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。

示例 1：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

示例 2：
输入：nums = [0,0,0], target = 1
输出：0
 
提示：
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
'''


### 方法一：相向双指针
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = inf
        n = len(nums)
        nums.sort()
        i = 0
        while i < n - 2:
            j, k = i + 1, n - 1
            while j < k:
                x, y, z = nums[i], nums[j], nums[k]
                tot = x + y + z
                res = tot if abs(tot - target) < abs(res - target) else res
                if tot == target:
                    return target
                elif tot > target:
                    while j < k and nums[k] == z:
                        k -= 1
                else:
                    while j < k and nums[j] == y:
                        j += 1
            while i < n - 2 and nums[i] == x:
                i += 1
        return res