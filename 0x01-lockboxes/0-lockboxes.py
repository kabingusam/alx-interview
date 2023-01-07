#!/usr/bin/python3
'''lockboxes
''' 

def canUnlockAll(boxes):
    seen = set()
    to_visit = [0]

    while to_visit:
        box = to_visit.pop()
        if box not in seen:
            seen.add(box)
            to_visit.extend(boxes[box])
        return len(seen) == len(boxes)
