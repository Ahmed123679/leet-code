# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      
        l1 = Solution.reverseListNode(l1) # revesre l1
        l2 =  Solution.reverseListNode(l2) # reverse 12
       
        num1 = Solution.getListNodeValue(l1)
        # print(num1)
        num2 = Solution.getListNodeValue(l2)
        # print(num2)
        result = num1 + num2
        RList = [int(x) for x in str(result)]
        RList.reverse()
        output:ListNode = ListNode(-1)
        for i in RList:
            Solution.appendListNode(output,i)
        return output
   
    def reverseListNode(head:ListNode):
        q,p,n = None,head,head.next
        while p != None:
            p.next = q
            q = p
            p = n
            n = n.next if n != None else None
        return q
    def getListNodeValue(head:ListNode)->int:
        p = head
        num:str = ''
        while p != None:
            num += str(p.val)
            p = p.next
        
        realNumber = int(num)
        return realNumber
    def appendListNode(head:ListNode,value:int):
        if head.val == -1 and head.next == None:
            head.val = value
        else:
            p = head
            while p.next != None:
                p = p.next
            p.next = ListNode(value)
    def printListNode(head:ListNode):
        p = head
        while p != None:
            print(p.val)
            p = p.next
            
    
            
