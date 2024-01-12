# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # my solution, easiest yet | Time: O(n) Space: O(1)
    def hasCycle(self, head: ListNode) -> bool:
        list_of_nodes = []
        while head:
            if head in list_of_nodes:
                return True
            else:
                list_of_nodes.append(head)
            head = head.next
            
        return False

