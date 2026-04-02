# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None        

        #basic iteration
        # newnode=ListNode(head.val,None)
        # curnode=head
        # while curnode.next is not None:
        #     curnode=curnode.next
        #     newnode=ListNode(curnode.val,newnode)
        
        # return newnode

        #improved iteration with pointer changes instead of making new nodes
        if head.next is None:
            return head
        
        prev=None
        cur=head
        while cur is not None:
            next_temp=cur.next #save pointer to next node
            cur.next=prev #reverse pointer on the current node
            cur,prev=next_temp,cur #move current to the saved reference to the next node and previous to the old current node
        
        return prev #returning prev because cur is none and prev is the last node that now points the right way