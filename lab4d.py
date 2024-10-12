#!/usr/bin/env python3

# Strings for testing
str1 = 'Hello Universe!!'
str2 = 'Seneca College'

def first_five(s):
    # Return the first five characters of the input string
    return s[:5]

def last_seven(s):
    # Return the last seven characters of the input string
    return s[-7:]

def middle_number(n):
    # Return the middle two digits from the string representation of a number
    s = str(n)
    return s[1:3]

def first_three_last_three(s1, s2):
    # Combine the first three characters of s1 with the last three characters of s2
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(1500))
    print(middle_number(1.50))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))

