#!/usr/bin/python3
'''lockboxes
''' 

def canUnlockAll(boxes):
    # stores the keys
    keys = set()

    # stores boxes to be opened
    stack = []

    # add first box to stack
    stack.append(boxes[0])

    # add keys of the first box to the set
    keys.update(boxes[0])

    while stack:
        # get box to open
        box = stack.pop

        # add keys of this box to the set
        keys.update(boxes)

        # loop through all the boxes
        for i in range(1, len(boxes)):
            if i not in keys and i in box:
                stack.append(boxes[i])

    return len(keys) == len(boxes) 
