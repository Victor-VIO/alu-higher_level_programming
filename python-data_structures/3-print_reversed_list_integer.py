#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints list in reverse"""
    if my_list is None:
        return
    for num in reversed(my_list):
        print("{:d}".format(num))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
    print_reversed_list_integer(None)  # Test None case
