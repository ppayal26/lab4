#!/usr/bin/env python3

def is_digits(s):
    # Return True if the string contains only digits, otherwise False
    return s.isdigit()

if __name__ == '__main__':
    # Test cases to verify the function
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(f"{item} contains only digits.")
        else:
            print(f"{item} contains non-digit characters.")

