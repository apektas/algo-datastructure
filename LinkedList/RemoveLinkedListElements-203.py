class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return head
        dummyHead = ListNode()
        dummyHead.next = head
        beforeNodeToRemove = dummyHead
        while beforeNodeToRemove.next:
            if beforeNodeToRemove.next.val == val:
                nodeToRemove = beforeNodeToRemove.next
                beforeNodeToRemove.next = nodeToRemove.next
            else:
                beforeNodeToRemove = beforeNodeToRemove.next

        return dummyHead.next


head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)

head = Solution().removeElements(head,3)

cur = head
while(cur):
    print(cur.val, end=",")
    cur = cur.next