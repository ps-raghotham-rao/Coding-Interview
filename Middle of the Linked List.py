# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        head1=head

        
        while(head.next!=None):
            head=head.next
            c+=1
        c+=1
        print(c)
        
        
        n=c//2
            
        i=0
        head=head1
        while(i<n):
            head=head.next
            i+=1
        return head
        
        
        
        #This is optional
        
        # ls=[]
        
        
#         while(head.next!=None):
#             ls.append(head.val)
#             head=head.next
#         ls.append(head.val)
#         print(ls)
#         return ls
            
        