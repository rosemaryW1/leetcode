class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node  # Fix: Update curr to the next_node
        return prev
# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Create a Solution instance
solution = Solution()

# Reverse the linked list
reversed_head = solution.reverse_list(head)

# Print the reversed linked list
while reversed_head:
    print(reversed_head.value, end=" ")
    reversed_head = reversed_head.next