'''
峰值元素是指其值严格大于左右相邻值的元素。
给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设 nums[-1] = nums[n] = -∞ 。
你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

示例 1：
输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。

示例 2：
输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5 
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

提示：
1 <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1
对于所有有效的 i 都有 nums[i] != nums[i + 1]
'''


### 方法一：遍历
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))


### 方法二：手写二分
# 时间复杂度：O(log n)
# 空间复杂度：O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        def get(i):
            if i == -1 or i == n:
                return -inf
            return nums[i]

        left, right = 0, n  # 左闭右开写法
        while left < right:
            mid = left + (right - left) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                return mid
            elif get(mid - 1) < get(mid):  # 此时有 get(mid - 1) < get(mid)，处于上升阶段
                left = mid + 1
            else:  # 此时有 get(mid - 1) > get(mid)
                right = mid  # right 是开区间，所以不能写 right = mid - 1
        return left