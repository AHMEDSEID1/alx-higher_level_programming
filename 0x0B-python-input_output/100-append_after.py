#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """
    Appends a line of text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to append after the lines containing the search string.

    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

        file.truncate()
