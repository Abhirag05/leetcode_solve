# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head
        #split into two
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #reverse the second half
        second=slow.next
        slow.next=None
        prev=None
        while second:
            next_node=second.next
            second.next=prev
            prev=second
            second=next_node
        
        #modify the linking
        first=head
        second=prev
        while second:
            f_next=first.next
            s_next=second.next
            first.next=second
            second.next=f_next
            first=f_next
            second=s_next

#approach: The algorithm consists of three main steps. First, we use the slow and fast pointer technique to find the middle of the linked list and split it into two halves. Second, we reverse the second half of the list. Finally, we merge the two halves by alternating nodes from each half.

#time complexity: O(n), where n is the number of nodes in the linked list. We traverse the list multiple times, but each traversal is linear.


#space complexity: O(1), as we are using a constant amount of extra space for the pointers.