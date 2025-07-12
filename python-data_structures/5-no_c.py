#!/usr/bin/python3
def no_c(my_string):
    """Removes all 'c' and 'C' characters"""
    result = ""
    for char in my_string:
        if char not in ('c', 'C'):
            result += char
    return result


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
