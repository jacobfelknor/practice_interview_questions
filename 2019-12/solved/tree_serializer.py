# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes
# the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

MAX_SIZE = 50


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeSerializer:
    """ 
        Class that serializes a given node.
        As of now, this serialization is just
        a str(list).
    """

    def __init__(self, node):
        self.__string = [None] * MAX_SIZE
        self.serialize(node)

    def getleft(self, index):
        return 2 * index + 1

    def getright(self, index):
        return 2 * index + 2

    def serialize_helper(self, root, index):
        """ recursive helper function to serialize the tree """
        self.__string[index] = root.val
        if root.left is not None:
            self.serialize_helper(root.left, self.getleft(index))

        if root.right is not None:
            self.serialize_helper(root.right, self.getright(index))

    def serialize(self, root):
        self.serialize_helper(root, 0)
        return self.__string

    def string(self):
        return str(self.__string)


class NodeDeserializer:
    """ 
        Class that deserializes a given node.
        This node must have been serialized 
        by the NodeSerializer class above
    """

    def __init__(self, string):
        self.node = Node(None)
        self.node_list = None
        self.deserialize(string)
        pass

    def getleft(self, index):
        return 2 * index + 1

    def getright(self, index):
        return 2 * index + 2

    def deserialize_helper(self, root, index):
        """ recursive helper function to deserialize the tree """
        left = self.node_list[self.getleft(index)]
        if left:
            root.left = Node(left)
            self.deserialize_helper(root.left, self.getleft(index))

        right = self.node_list[self.getright(index)]
        if right:
            root.right = Node(right)
            self.deserialize_helper(root.right, self.getright(index))

    def deserialize(self, string):
        self.node_list = eval(
            string
        )  # I know this can be dangerous... may change later
        self.node.val = self.node_list[0]
        self.deserialize_helper(self.node, 0)

    def object(self):
        return self.node


if __name__ == "__main__":
    main_node = Node(
        "root",
        Node(
            "left",
            Node("left.left", Node("left.left.left"), Node("left.left.right")),
            Node("left.right"),
        ),
        Node("right", Node("right.left"), Node("right.right")),
    )

    tree_string = NodeSerializer(main_node).string()
    tree_obj = NodeDeserializer(tree_string).object()
    new_string = NodeSerializer(tree_obj).string()

    print(new_string)

    # given test case:
    assert (
        NodeDeserializer(NodeSerializer(main_node).string()).object().left.left.val
        == "left.left"
    )

    print("It works!")
