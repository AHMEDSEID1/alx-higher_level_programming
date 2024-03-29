#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of \
2 positive "
                                "integers")
        self.__position = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 positive "
                                "integers")
        self.__position = value

    def area(self):
        return int(self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size + self.__position[1]):
                if i < self.__position[1]:
                    print()
                    continue
                for j in range(0, self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        print(' ', end='')
                        continue
                    print('#', end='')
                print()

    def __str__(self):
        string = ''
        if self.__size == 0:
            return string
        else:
            for i in range(0, int(self.__size) + self.__position[1]):
                if i < self.__position[1]:
                    string += '\n'
                    continue
                for j in range(0, int(self.__size) + self.__position[0]):
                    if j < self.__position[0]:
                        string += ' '
                        continue
                    string += '#'
                if i != self.__size + self.__position[1] - 1:
                    string += '\n'
        return string

    def __lt__(self, other):
        return Square.area(self) < Square.area(other)

    def __le__(self, other):
        return Square.area(self) <= Square.area(other)

    def __eq__(self, other):
        return Square.area(self) == Square.area(other)

    def __ne__(self, other):
        return Square.area(self) != Square.area(other)

    def __gt__(self, other):
        return Square.area(self) > Square.area(other)

    def __ge__(self, other):
        return Square.area(self) >= Square.area(other)
