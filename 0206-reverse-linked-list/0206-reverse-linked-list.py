# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
    #     return recursive

    # def recursive(self, curnode, lastval)
    #     if curnode.next is None:
        

        newnode=ListNode(head.val,None)
        curnode=head
        while curnode.next is not None:
            curnode=curnode.next
            newnode=ListNode(curnode.val,newnode)
        
        return newnode