# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

        
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        sumVal = l1.val + l2.val
        if sumVal < 10:
            sumNode = ListNode(sumVal)
            sumNode.next = self.addTwoNumbers(l1.next, l2.next)
            return sumNode
        else:
            sumNode = ListNode(sumVal-10)
            sumNode.next = self.addTwoNumbers(ListNode(1),self.addTwoNumbers(l1.next, l2.next))
            return sumNode
