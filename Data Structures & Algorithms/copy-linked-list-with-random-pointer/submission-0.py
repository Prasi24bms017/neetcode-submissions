"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        old_to_new={}
        curr=head
        while curr is not None:
             old_to_new[curr]=Node(curr.val)
             curr=curr.next
        curr=head
        while curr is not None:
            new_node= old_to_new[curr]
            if curr.next is not None:
                new_node.next= old_to_new[curr.next]
            else:
                new_node.next=None
            if curr.random is not None:
                new_node.random= old_to_new[curr.random]
            else:
                new_node.random=None
            curr=curr.next
        return old_to_new[head]
            

            

        