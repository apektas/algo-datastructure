class ListNode(object):
    def __init__(self, x=-1):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoList(self, l1, l2):
        carryOver = 0;
        head = ListNode();
        current = head
        while l1 and l2:
            val = carryOver + l1.val + l2.val
            current.next = ListNode(val%10)
            carryOver = val //10
            l1 = l1.next
            l2 = l2.next
            current = current.next

        while l1 or l2:
            val = l1.val if l1 else l2.val
            val = carryOver + val
            current.next = ListNode(val%10);
            carryOver = val // 10
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
            current = current.next

        if(carryOver):
            current.next = ListNode(carryOver)

        return head.next

    def addingNumbersReverseNotAllowed(self, l1: ListNode, l2:ListNode) -> ListNode:
        from collections import deque
        l1Stack = deque()
        l2Stack = deque()

        l1Cur = l1
        l2Cur = l2

        while l1Cur or l2Cur:
            if l1Cur:
                l1Stack.appendleft(l1Cur)
                l1Cur = l1Cur.next
            if l2Cur:
                l2Stack.appendleft(l2Cur)
                l2Cur = l2Cur.next

        result = []
        carryOver = 0
        while len(l1Stack) or len(l2Stack):
            val = carryOver
            if len(l1Stack): val+=l1Stack.popleft().val
            if len(l2Stack): val+=l2Stack.popleft().val
            carryOver =  val // 10
            result.append(val%10)

        if carryOver:
            result.append(carryOver)

        cur = dummyHead = ListNode()

        for i in result[::-1]:
            cur.next = ListNode(i)
            cur = cur.next

        return dummyHead.next



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sum = Solution().addTwoList(l1,l2)
#
# while(sum):
#     print(sum.val)
#     sum = sum.next


l1 = ListNode(7)


l2 = ListNode(5)


sum = Solution().addingNumbersReverseNotAllowed(l1,l2)

while(sum):
    print(sum.val)
    sum = sum.next
