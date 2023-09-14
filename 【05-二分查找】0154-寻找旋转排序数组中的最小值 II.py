'''
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
你必须尽可能减少整个过程的操作步骤。

示例 1：
输入：nums = [1,3,5]
输出：1

示例 2：
输入：nums = [2,2,2,0,1]
输出：0
 
提示：
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
'''


### 方法一：遍历
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
        
        
### 方法二：手写二分
# 时间复杂度：O(n)  # 最坏情况下可能是O(n)
# 空间复杂度：O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1  # 左闭右闭写法
        while left < right:  # 循环结束条件为 left == right
            mid = left + (right - left) // 2
            if nums[mid] == nums[right]:  # 排除右端点
                right -= 1
            elif nums[mid] > nums[right]:  # 左区间递增，排除左边
                left = mid + 1
            else:  # 右区间递增，排除右边
                right = mid
        return nums[left]