#!/usr/bin/env python3

def join_lists(l1, l2):
    # Combine both lists, remove duplicates, and return the result
    return list(set(l1).union(set(l2)))

def match_lists(l1, l2):
    # Return elements that are common in both lists
    return list(set(l1).intersection(l2))

def diff_lists(l1, l2):
    # Return elements that are unique in either list (symmetric difference)
    return list(set(l1).symmetric_difference(set(l2)))

if __name__ == '__main__':
    lst1 = list(range(1, 10))
    lst2 = list(range(5, 15))
    print('lst1: ', lst1)
    print('lst2: ', lst2)
    print('joined: ', join_lists(lst1, lst2))
    print('common: ', match_lists(lst1, lst2))
    print('unique: ', diff_lists(lst1, lst2))


