# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_length(self, node):
        l = 0
        while node:
            l += 1
            node = node.next
        return l
    
    def add_two_numbers_helper(self, l1, l2):
        if not l1 and not l2:
            return 0, None

        # Recursively add smaller parts of the numbers
        carry, next_node = self.add_two_numbers_helper(l1.next if l1 else None, l2.next if l2 else None)

        # Add current digits
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = carry + val1 + val2
        carry = total // 10
        current_node = ListNode(total % 10)
        current_node.next = next_node

        return carry, current_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1 = self.get_length(l1)
        len2 = self.get_length(l2)
        while len1 < len2:
            l1 = ListNode(0, l1)
            len1 += 1
        while len2 < len1:
            l2 = ListNode(0, l2)
            len2 += 1
        
        carry, result_head = self.add_two_numbers_helper(l1, l2)
        if carry:
            result_head = ListNode(carry, result_head)
        
        return result_head
