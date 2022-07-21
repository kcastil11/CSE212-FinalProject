class BST:
    """
    Implement the Binary Search Tree (BST) data structure. We will create
    a inner class of node for the BST class.
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree if there happens to be any. 
        """

        def __init__(self, data):
            """
            Initialize the node class.
            """
            self.data = data
            self.left = None
            self.right = None


    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None


    def insert(self, data):
        """
        This method will check if the root is None.
        The reason for this is because if the BST is empty,
        it will make the node the root. If the BST is not empty,
        traverse through the tree to find the spot to add the node.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root


    def _insert(self, data, node):
        """
        This function is looking for a place to insert a node to 
        the BST. If the user tries to add a number that is not
        unique, it will return ending the _insert method.

        There has been added mistakes to the code for you to figure out.
        Hint: Use pen and paper to draw the insert function, and see what is
        acutally happening. Are they going to the right spots?
        """
        if data == node.data:
            return

        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
                

    def empty(self):
        """
        Return True if tree is empty, return false
        if not empty.
        """
        # pass
        return self.root is None


    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root


    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """

        #Base Case #1: Data is not in tree
        if node is None:
            return False

        #Base Case #2: Data is in the tree.
        elif data == node.data:
            return True

        # Smaller problem: Recurse through the tree.
        else:
            if data < node.data:
                return self._contains(data, node.left)
            else:
                return self._contains(data, node.right)


    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root

    def _traverse_forward(self, node):
        """
        This function allows us to iterate through
        the BST and output the tree in order.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)


    def get_sum(self):
        """
        Get the sum of the right subtree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_sum(self.root)


    def _get_sum(self, node):

        """
        Traverse through the BST and add all the data together.

        Find the sum of all the node's data and return the total.
        Hint: traverse through the left sub-tree and get the sum, 
        traverse through the right sub-tree and get the sum, after that
        is done add the node, left sub-tree sum, and the right sub-tree sum
        together to get the sum of the whole tree.
        """
        total, left, right = 0, 0, 0

        if node is None:
            return 0
        else:

            # Recurse through the left side
            if node.left != None:
                left = self._get_sum(node.left)

            # Recurse through the right side
            if node.right != None:
                right = self._get_sum(node.right)

            # Add them all together
            total = node.data + left + right

        return total


print("\n=========== PROBLEM 1 TESTS ===========")
tree = BST()
tree.insert(2)
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.insert(5)
tree.insert(6)

# Output: 1, 2, 3, 4, 5, 6
for x in tree: 
    print(x) 


print("\n=========== PROBLEM 2 TESTS ===========")
print(tree.empty()) # Output: False

# Create an empty tree.
tree2 = BST()
print(tree2.empty()) # Output: True
tree2.insert(6)
tree2.insert(30)
tree2.insert(-17)
tree2.insert(89)
print(tree2.empty())  # Output: False

print("\n=========== PROBLEM 3 TESTS ===========")
print(99 in tree2) # False
print(30 in tree2) # True
print(65 in tree2) # False
print(6 in tree2) # True

print("\n=========== PROBLEM 4 TESTS ===========")
tree3 = BST()
tree3.insert(15)
tree3.insert(4)
tree3.insert(81)
tree3.insert(90)
tree3.insert(-10)
tree3.insert(-5)
tree3.insert(8)
print("Sum of tree1 is: " + str(tree.get_sum())) # Output: 21
print("Sum of tree2 is: " + str(tree2.get_sum())) # Output: 108
print("Sum of tree3 is: " + str(tree3.get_sum())) # Output: 183
