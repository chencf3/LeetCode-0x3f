'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
 
提示：
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums 是一个非递减数组
-10^9 <= target <= 10^9
'''


### 方法一：遍历
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        for i, x in enumerate(nums):
            if x == target:
                if res[-1] == -1:
                    res = [i, i]
                else:
                    res[1] = i
            elif x > target:
                return res
        return res


### 方法二：调用bisect函数
# 时间复杂度：O(log n)
# 空间复杂度：O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        left = bisect_left(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect_right(nums, target)
        return [left, right - 1]


### 方法三：手写二分
# 时间复杂度：O(log n)
# 空间复杂度：O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(target):
            '''
            返回第一个大于等于target的位置
            '''
            left, right = 0, len(nums)  # 左闭右开写法
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        x = lower_bound(target)
        if x >= len(nums) or nums[x] != target:
            return [-1, -1]
        return [x, lower_bound(target + 1) - 1]
    
'''
(1) >= x:
lower_bound(x)
(2) > x:
lower_bound(x + 1)
(3) < x:
lower_bound(x) - 1
(4) <= x:
lower_bound(x + 1) - 1
'''