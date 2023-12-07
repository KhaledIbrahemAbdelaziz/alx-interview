#!/usr/bin/python3
"""LockBoxes problem"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened.
    boxes (list): list of lists
    return:
    True: all can unlock.
    False: all boxes can't unlock.
    """
    length = len(boxes)
    keys = set()
    unlock_boxes = []
    i = 0

    while i < length:
        oldi = i
        unlock_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in unlock_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in unlock_boxes and i != 0:
            return False
    return True
