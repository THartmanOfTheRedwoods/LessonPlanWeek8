#!/usr/bin/env python3

def half_mirror(str_in):
    """Write a function `half_mirror(str_in)` that takes a string input and creates
    a mirrored version of its first half. If the string has an odd number of
    characters, consider only the first half (ignoring the middle character). Return
    the mirrored half as a new string."""
    half_str_in = str_in[0:len(str_in)//2]
    return ''.join(reversed(half_str_in))

print(half_mirror('PythonProgramming'))

import re

def count_pattern_occurrences(text, pattern):
    """Create a function `count_pattern_occurrences(text, pattern)` that counts how
    many times a specified pattern appears in a given text, using regular expressions."""
    # The below for loop is just for demonstration, the soltuion is really the return line
    for match in re.finditer(pattern, text, re.IGNORECASE):
        print(f"Found '{match.group()}' at position {match.start()}")

    return len( re.findall( pattern, text, re.IGNORECASE ) )

print(f'FOUND {count_pattern_occurrences('The cat chased the mouse.', r"\bthe\b")} occurrences of the pattern.')

def find_all_and_replace(infile, outfile, search_pattern, replace_word):
    with open(infile, 'r') as in_f, open(outfile, 'w') as out_f:
        for line in in_f:
            out_f.write(re.sub(search_pattern, replace_word, line, flags=re.IGNORECASE))


find_all_and_replace('files/NewColossus.txt', 'files/OldColossus.txt', r'the', r'a')

def list_union_fancy(list1, list2):
    """ Write a function that takes two lists, combines them, and then removes any
        duplicates. The function should return the modified list. """
    return list(set(list1).union(set(list2)))

def list_union(list1, list2):
    """ Write a function that takes two lists, combines them, and then removes any
        duplicates. The function should return the modified list. """
    for item in list2:
        if item not in list1:
            list1.append(item)
    return list1

print(list_union(['abc', 'def', 'ghi', 'xyz'], ['abc', 'tuv', 'xyz']))

def loop_reverse(list1):
    """ Write a function that takes a list and returns a new list with the elements
    in reverse order without using the reverse() method or slicing. Instead, use a
    loop to achieve the reversal. """
    list2 = list()
    for item in list1:  # One method is to keep inserting at the beginning of the new list.
        list2.insert(0, item)
    return list2

def loop_reverse_v2(list1):
    """ Write a function that takes a list and returns a new list with the elements
    in reverse order without using the reverse() method or slicing. Instead, use a
    loop to achieve the reversal. """
    list2 = list()
    for i in range(len(list1) - 1, -1, -1):  # Another method is to go backwards through the list
        list2.append(list1[i])
    return list2


print(loop_reverse(['abc', 'def', 'ghi', 'xyz']))
print(loop_reverse_v2(['abc', 'def', 'ghi', 'xyz']))