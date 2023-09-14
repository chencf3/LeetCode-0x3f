'''
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。

示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。

示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。

提示：
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
'''


### 方法一：相向双指针，没考虑重复数字，添加到答案时去重
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res


### 方法二：相向双指针，考虑重复数字
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n, i = len(nums), 0
        while i < n - 2:
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[-2] + nums[-1] < 0:
                x = nums[i]
                while i < n - 2 and nums[i] == x:
                    i += 1
                continue
            left, right = i + 1, n - 1
            while left < right:
                x, y, z = nums[i], nums[left], nums[right]
                if x + y + z == 0:
                    res.append([x, y, z])
                    while left < right and nums[left] == y:
                        left += 1
                    while left < right and nums[right] == z:
                        right -= 1
                elif x + y + z > 0:
                    while left < right and nums[right] == z:
                        right -= 1
                else:
                    while left < right and nums[left] == y:
                        left += 1
            while i < n - 2 and nums[i] == x:
                i += 1
        return res