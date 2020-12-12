class ListNode(object):
    def __init__(self, x=-1):
        self.val = x
        self.next = None

# https://leetcode.com/problems/insertion-sort-list/discuss/920371/Python-Insertion-Sort-explained

class Solution(object):
    def insertionSortList(self, head):
        dummyHead = ListNode(0)
        dummyHead.next = nodeToInsert = head

        while head and head.next:
            if head.val > head.next.val:
                # Locate nodeToInsert.
                nodeToInsert = head.next
                # Locate nodeToInsertPre.
                nodeToInsertPre = dummyHead
                while nodeToInsertPre.next.val < nodeToInsert.val:
                    nodeToInsertPre = nodeToInsertPre.next

                head.next = nodeToInsert.next
                # Insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next.
                nodeToInsert.next = nodeToInsertPre.next
                nodeToInsertPre.next = nodeToInsert
            else:
                head = head.next
        return dummyHead.next



    def insertionSort(self, head):
        dummyHead = ListNode(0)
        dummyHead.next = cur = head
        nodeToInsert = dummyHead
        while cur and cur.next:
            if cur.next.val < cur.val:
                # delete link
                nodeToInsert = cur.next

                nodePrev = dummyHead

                ## find previous link
                while nodePrev.next.val < nodeToInsert.val:
                    nodePrev = nodePrev.next

                ## delete link and create new links
                cur.next = nodeToInsert.next
                nodeToInsert.next = nodePrev.next
                nodePrev.next = nodeToInsert

            else:
                cur = cur.next

        return dummyHead.next



head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(1)


cur = head
while(cur):
    print(cur.val, end=",")
    cur = cur.next

print("deneme")
#cur = Solution().insertionSortList(head)
cur = Solution().insertionSort(head)
while(cur):
    print(cur.val, end=",")
    cur = cur.next