#!/usr/bin/python3

"""
newList = []
itetate through list:
    if elem is list:
        iterate list:
            if elem <= lis1.length and elem not in newList:
                newList.append(elem)
            else throw error
    else not list:
        if elem <= lis1.length and elem not in newList:
                newList.append(elem)
    if elem in newList
method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True

    keys = boxes[0]
    for key in keys:
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    return all(unlocked)
  