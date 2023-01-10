#!/usr/bin/python3
'''0-minoperations.py
'''

def minOperations(n: int) -> int:
    '''
    Computes the fewest number of copy-paste operations needed to result in exactly n H characters.
    :param n: the number of Hs we want to reach in the text file
    :return: returns the number of operations needed to reach n Hs, 0 if n <= 1 or n is not int
    '''
    ans = 0
    if n <= 1:
        return 0
    while n % 2 == 0:
        n = n // 2
        ans += 1
    return ans + 1
