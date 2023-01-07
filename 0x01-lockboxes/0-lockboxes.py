#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''This a method determines if all the boxes can be opened.
    '''
    n = len(boxes)
    seen = set([0])
    unseen = set(boxes[0]).difference(set([0]))
    while len(unseen) > 0:
        boxIdx = unseen.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen.add(boxIdx)
    return n == len(seen)
