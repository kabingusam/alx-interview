#!/usr/bin/python3
'''0-minoperations.py
'''

def minOperations(n: int) -> int:
    '''
    Computes the fewest number of copy-paste operations needed to result in exactly n H characters.
    :param n: the number of Hs we want to reach in the text file
    :return: returns the number of operations needed to reach n Hs, 0 if n <= 1 or n is not int
    '''
    if n <= 0:
        return 0
    steps = 0
    while n > 1:
        i = 2
        while i * i <= n:
            if n % i == 0:
                n = n // i
                steps += i
                break
            i += 1
        if i * i > n:
            n = n - 1
            steps += 1
    return steps
