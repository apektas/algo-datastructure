class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## single pass solution!!! think about fast fast fast!!!
## more cleaver way to remove node = current = current.next.next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = self.calculateLength(head)
        nodeToRemove = length - n
        dummyHead = ListNode(-1)
        dummyHead.next = head
        previous = dummyHead
        cur = head
        i = 0
        while cur:
            if i == nodeToRemove:
                nextNode = cur.next
                previous.next = nextNode
                cur = cur.next
                break
            else:
                previous = cur
                cur = cur.next
            i+=1

        return dummyHead.next


    def calculateLength(self, head):
        length = 0
        fast = head
        while fast and fast.next:
            length+=1
            fast = fast.next.next
        length *=2
        if fast:
            length += 1
        return length

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

print(Solution().calculateLength(None))
res = Solution().removeNthFromEnd(l1,1)
while res:
    print(res.val)
    res = res.next

