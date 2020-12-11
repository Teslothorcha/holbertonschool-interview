#!/usr/bin/python3
"""
    Validates if all boxes can be openned
    @boxes: list of lists
    Returns: True or False
"""

def canUnlockAll(boxes):
    to_open = [i for i in range(len(boxes))]
    opened = {"0": "ok"}
    for box in range(len(boxes)):
        for key in boxes[box]:
            if key in to_open and key != box:
                if key not in opened:
                    opened["{}".format(key)] = "ok"
    for k in to_open:
        if str(k) not in opened:
            return False
    return True
