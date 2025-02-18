# User function Template for python3
'''
    Your task is to delete the given node from
    the linked list, without using head pointer.

    Function Arguments: node (given node to be deleted)
    Return Type: None, just delete the given node from the linked list.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''


class Solution:
    # Function to delete a node without any reference to head pointer.
    def deleteNode(self, curr_node):
        # code here
        temp = curr_node.next
        curr_node.data = temp.data
        curr_node.next = temp.next


# Time Complexity = O(1).
# Space complexity : O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : No
