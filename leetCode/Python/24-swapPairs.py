# Time:  O(n)
# Space: O(1)
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.
#


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # @param a ListNode
    # @return a ListNode
    def print_llst(self, head):
        llst = ""
        while head != None:
            llst += str(head.val) + ' '
            head = head.next
        print llst

    def swapPairs(self, head):
        dummy = ListNode(-1); dummy.next = head; dum = dummy
        while dum.next and dum.next.next:
            tmp = dum.next.next
            dum.next.next = tmp.next
            tmp.next = dum.next
            dum.next = tmp
            dum = dum.next.next
        return dummy.next

if __name__ == '__main__':
   s = Solution()
   test_llst = ListNode(1)
   test_llst.next = ListNode(2)
   test_llst.next.next  = ListNode(3)
   test_llst.next.next.next = ListNode(4)
   test_llst.next.next.next.next = ListNode(5)
   # print s.llst_length(test_llst)
   s.print_llst(test_llst)
   s.print_llst(s.swapPairs(test_llst))









        