# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        #split
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reverse
        prev=None
        while slow:
            next_node=slow.next
            slow.next=prev
            prev=slow
            slow=next_node

        while prev:
            if prev.val!=head.val:
                return False
            prev=prev.next
            head=head.next
        return True
        
#Approach:
# 1. We will use the slow and fast pointer technique to find the middle of the linked list. The slow pointer will move one step at a time, while the fast pointer will move two steps at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle.
# 2. We will then reverse the second half of the linked list starting from the slow pointer. We will maintain three pointers: prev (initially None), slow (initially at the middle), and next_node (to store the next node). In each iteration, we will update the next pointer of slow to point to prev, then move prev and slow one step forward.
# 3. Finally, we will compare the values of the nodes in the first half of the linked list (starting from head) with the values of the nodes in the reversed second half (starting from prev). If all values match, we will return True, indicating that the linked list is a palindrome. Otherwise, we will return False.

#time complexity: O(n), where n is the number of nodes in the linked list. We need to traverse the entire list twice (once to find the middle and once to reverse the second half).

#space complexity: O(1), as we are using a constant amount of extra space for the pointers.