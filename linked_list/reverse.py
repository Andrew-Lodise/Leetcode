# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # leetcode itterative solution| Time: O(n) Space: O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        cur_node = head
        while cur_node:
            nxt_node = cur_node.next    # storing the next node before chaning pointer
            cur_node.next = prev_node   # changing current pointer to previous node
            prev_node = cur_node        # iterating prev node
            cur_node = nxt_node         # iterating cur node

        return prev_node
    
e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

mysol = Solution()
print(mysol.reverseList(a))

#scap notes
myList = [a, b, c]

# easy way to loop
cur_node = a
while cur_node != None:
    #print(cur_node.val)

    #update
    cur_node = cur_node.next