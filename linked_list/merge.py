# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # my solution! probably too long. | Time: O(list1 + list2)/O(n) Space O(n)
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        new_list = None # setting a starting new list
        # deciding on the new head
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            new_list = ListNode(list2.val)
            list2 = list2.next
        elif list2 == None:
            new_list = ListNode(list1.val)
            list1 = list1.next
        elif list1.val <= list2.val:
            new_list = ListNode(list1.val)
            list1 = list1.next
        else:
            new_list = ListNode(list2.val)
            list2 = list2.next
        #print("new_list =", new_list.val)

        # saving new head to return later
        new_head = new_list

        # looping through both
        while list1 or list2:
            # these two manage if one list gets emptied
            if list1 == None:
                new_list.next = list2
                list2 = list2.next
            elif list2 == None:
                new_list.next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            
            new_list = new_list.next
        
        return new_head

    #leetcode solution, uses a dummy node to deal with edge cases, but pretty much the same
    def mergeTwoLists2(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

list1 = ListNode(1, ListNode(3, ListNode(8, ListNode(10))))
list2 = ListNode(2, ListNode(4, ListNode(6, ListNode(10))))

mysol = Solution()
finished_head = mysol.mergeTwoLists(list1, list2)
while finished_head:
    print(finished_head.val)
    finished_head = finished_head.next
#scrap notes


#new_list = None

# deciding on the new head
#if list1.val <= list2.val:
    #new_list = ListNode(list1.val)
    #list1 = list1.next
#else:
    #new_list = ListNode(list2.val)
    #list2 = list2.next
#print("new_list =", new_list.val)

# saving new head to return later
#new_head = new_list

# looping through both
#while list1 and list2:
    #print("list1 =", list1.val, "list2 =", list2.val)
    #if list1.val <= list2.val:
        #new_list.next = list1
        #list1 = list1.next
    #else:
        #new_list.next = list2
        #list2 = list2.next
    
    #new_list = new_list.next

#while new_head:
    #print(new_head.val)
    #new_head = new_head.next