#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer in a list"""
    if not my_list:
        return None
    max_num = my_list[0]
    for num in my_list:
        if num > max_num:
            max_num = num
    return max_num


if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
