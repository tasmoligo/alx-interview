#!/usr/bin/python3
'''
Determines if all boxes can be opened. A key with the same number as a box
opens that box. There can be keys that do not have boxes.
The first box, boxes[0] is unlocked.

Args:
     boxes - a list of list

Return: True if all boxes can be opened,
        otherwise, false
'''


def canUnlockAll(boxes):
    '''returns true if all boxes can be opened.'''
    openedBox = set([0])

    boxStack = [0]
    while boxStack:
        current_box = boxStack.pop()
        for key in boxes[current_box]:
            if key not in openedBox and key < len(boxes):
                openedBox.add(key)
                boxStack.append(key)
    return len(openedBox) == len(boxes)
