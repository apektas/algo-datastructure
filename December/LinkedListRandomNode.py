#Definition for singly-linked list.
from random import random
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        curNode = self.head
        result, counter = -1, 1
        while curNode:
            if random() < 1/counter:
                result = curNode.val

            counter+=1
            curNode = curNode.next

        return result




# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()