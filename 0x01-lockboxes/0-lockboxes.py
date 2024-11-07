#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Determines if all boxes can be opened starting from box 0.
    '''
    n = len(boxes)
    opened_boxes = {0}  # Start with box 0 opened
    keys_to_check = set(boxes[0])  # Keys initially in box 0

    while keys_to_check:
        box_index = keys_to_check.pop()  # Get a box to try to open
        # Check if the box is within range and hasn't been opened yet
        if box_index >= n or box_index in opened_boxes:
            continue
        # Open the box
        opened_boxes.add(box_index)
        # Add the keys found in the box to the set of boxes to explore
        keys_to_check.update(boxes[box_index])

    # If all boxes are opened, opened_boxes should have all indices from 0 to n-1
    return len(opened_boxes) == n
