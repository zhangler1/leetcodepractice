from collections  import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        activeService =deque()
        reserveService  =deque()
        activeService.append(root)
        prenode=None
        while(not len(activeService)==0):

            node=activeService.popleft()
            if(prenode):
                prenode.next=node

            if(node.left):
                reserveService.append(node.left)
            if(node.right):
                reserveService.append(node.right)


            prenode=node
            if len(activeService)==0 and not len(reserveService)==0:
                activeService.extend(reserveService.copy())
                reserveService.clear()
                prenode=None
        return root
                