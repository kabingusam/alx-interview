#!/usr/bin/python3
'''0-minoperations.py
'''

def minOperations(n: int) -> int:
    '''
    Computes the fewest number of copy-paste operations needed to result in exactly n H characters.
    :param n: the number of Hs we want to reach in the text file
    :return: returns the number of operations needed to reach n Hs, 0 if n <= 1 or n is not int
    '''
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            done += clipboard
            ops_count += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return ops_count