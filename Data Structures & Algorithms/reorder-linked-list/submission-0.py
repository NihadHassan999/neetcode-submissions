#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        def find_middle(node):
            fast = slow = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverselist(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node 
            return prev

        def mergelist(l1,l2):
            while l2:
                next1 = l1.next
                next2 = l2.next
                l1.next = l2
                l2.next = next1
                l1 = next1
                l2 = next2
        if not head or not head.next:
            return 
        
        middle = find_middle(head)
        second_half = middle.next
        middle.next = None

        second_half = reverselist(second_half)
        mergelist(head, second_half)