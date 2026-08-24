# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val:
            head=head.next
        if not head:
            return None
        prev=head
        curr=head.next
        while curr:
            if curr.val==val:
                prev.next=curr.next
                curr=curr.next
            else:
                prev=curr
                curr=curr.next
        return head

#Approach:
# 1. We will first check if the head node itself needs to be removed. If it does, we will move the head pointer to the next node until we find a node that does not need to be removed or reach the end of the list.
# 2. We will then traverse the rest of the linked list using two pointers, prev and curr. The prev pointer will point to the last node that does not need to be removed, and the curr pointer will traverse the list.
# 3. If the curr node needs to be removed, we will update the next pointer of the prev node to skip the curr node. If the curr node does not need to be removed, we will move both pointers forward.
# 4. Finally, we will return the head of the modified linked list.

#time complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once.

#space complexity: O(1), as we are using a constant amount of extra space.