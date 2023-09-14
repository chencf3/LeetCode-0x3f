'''
整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1

提示：
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-10^4 <= target <= 10^4
'''


### 方法一：遍历
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, x in enumerate(nums):
            if x == target:
                return i
        return -1


### 方法二：手写二分
# 时间复杂度：O(log n)
# 空间复杂度：O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1  # 左闭右闭写法
        while left < right:  # 循环结束条件为 left == right
            mid = left + (right - left) // 2
            if nums[mid] == target:  # mid 正好等于 target
                return mid
            elif nums[mid] > nums[right]:  # 左区间递增
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:  # 右区间递增
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return left if nums[left] == target else -1