'''
Created on Feb 4, 2017

@author: MT
'''

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        lastHead = root
        lastCurrent = None
        currentHead = None
        while lastHead:
            lastCurrent = lastHead
            while lastCurrent:
                if not currentHead:
                    currentHead = lastCurrent.left
                    current =  lastCurrent.left
                else:
                    current.next = lastCurrent.left
                    current = current.next
                if currentHead:
                    current.next = lastCurrent.right
                    current = current.next
                lastCurrent = lastCurrent.next
            lastHead = currentHead
            currentHead = None
    
    def test(self):
        pass