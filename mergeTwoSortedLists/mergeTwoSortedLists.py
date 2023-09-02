# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = dummy = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                result.next = list1
                result = result.next
                list1 = list1.next
            else:
                result.next = list2
                result = result.next
                list2 = list2.next
        
        if list1 or list2:
            if list1:
                result.next = list1
            else:
                result.next = list2

        return dummy.next
