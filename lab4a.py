#!/usr/bin/env python3

def join_sets(s1, s2):
    # Merge both sets and return a combined set with all unique elements
    return s1.union(s2)

def match_sets(s1, s2):
    # Return the common elements found in both s1 and s2
    return s1.intersection(s2)

def diff_sets(s1, s2):
    # Return a set with elements that are exclusive to each set
    return s1.symmetric_difference(s2)

if __name__ == '__main__':
    set_a = set(range(1, 10))
    set_b = set(range(5, 15))
    print('set_a: ', set_a)
    print('set_b: ', set_b)
    print('combined: ', join_sets(set_a, set_b))
    print('intersection: ', match_sets(set_a, set_b))
    print('unique: ', diff_sets(set_a, set_b))



