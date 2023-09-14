'''
给定一个单链表 L 的头节点 head ，单链表 L 表示为：
L[0] → L[1] → … → L[n-1] → L[n]
请将其重新排列后变为：
L[0] → L[n] → L[1] → L[n-1] → L[2] → L[n-2] → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1：
输入：head = [1,2,3,4]
输出：[1,4,2,3]

示例 2：
输入：head = [1,2,3,4,5]
输出：[1,5,2,4,3]

提示：
链表的长度范围为 [1, 5 * 10^4]
1 <= node.val <= 1000
'''


### 方法一：将链表的后半部分反转
# 时间复杂度：O(n)
# 空间复杂度：O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middleNode(head)  # 0876-链表的中间结点
        head2 = self.reverseList(mid)  # 0206-反转链表，将链表的后半部分反转
        # head, head.next, ..., head2.next, head2
        while head2.next:  # 结束条件是head2没有子节点
            nxt = head.next
            nxt2 = head2.next
            head2.next = nxt
            head.next = head2
            head = nxt
            head2 = nxt2