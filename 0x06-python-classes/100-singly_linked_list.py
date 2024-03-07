class Node:
    """
    Represents a node of a singly linked list.

    Private instance attributes:
        - __data: The data stored in the node.
        - __next_node: The reference to the next node in the linked list.

    Properties:
        - data: Retrieves the data of the node.
        - next_node: Retrieves the next_node of the node.

    Instantiation:
        Node(data, next_node=None)

    Raises:
        - TypeError: If data is not an integer or next_node is not a Node object.
    """

    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Args:
            - value: The data to be set.

        Raises:
            - TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next_node of the node.

        Args:
            - value: The next_node to be set.

        Raises:
            - TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """
        Returns a string representation of the node.

        Returns:
            - A string representation of the node's data.
        """
        return str(self.__data)


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Private instance attribute:
        - __head: The head node of the linked list.

    Instantiation:
        SinglyLinkedList()

    Public instance method:
        - sorted_insert(value): Inserts a new Node into the correct sorted position in the list.

    """

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Args:
            - value: The value of the new Node to be inserted.

        Raises:
            - TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        tmp = self.__head

        if tmp is None:
            self.__head = Node(value)
        elif tmp.data > value:
            new = Node(value, tmp)
            self.__head = new
        else:
            while tmp.next_node is not None:
                if tmp.next_node.data > value:
                    break
                tmp = tmp.next_node
            new = Node(value, tmp.next_node)
            tmp.next_node = new

    def __str__(self):
        """
        Returns a string representation of the singly linked list.

        Returns:
            - A string representation of the linked list, with each node's value on a separate line.
        """
        string = ''
        if self.__head is None:
            return string
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data) + '\n'
            tmp = tmp.next_node
        return string[:-1]
