class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The reference to the next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The reference to the next node. Defaults to None.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value (int): The new value to be set.
        
        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the reference to the next node.

        Returns:
            Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node.

        Args:
            value (Node): The new node to be set as the next node.
        
        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value in a sorted manner into the linked list.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)
