#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        no = ListNode(0)
        aux = no
        
        while list1 and list2:
            if list1.val < list2.val:
                aux.next = list1
                list1 = list1.next
            else:
                aux.next = list2
                list2 = list2.next
            aux = aux.next
        
        if list1:
            aux.next = list1
        else:
            aux.next = list2
        
        return no.next
