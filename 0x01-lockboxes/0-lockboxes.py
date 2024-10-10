#!/usr/bin/python3
"""
Module to determine if all lockboxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    
    Args:
        boxes (list of lists): A list where each sublist contains keys to open other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # Number of boxes
    n = len(boxes)

    # A set to keep track of unlocked boxes, starting with the first box
    unlocked = set([0])

    # A list to keep track of keys we have to unlock other boxes
    keys = boxes[0].copy()

    while keys:
        # Get the next key from the list of keys
        key = keys.pop(0)

        # If the key opens a box we haven't opened yet
        if key not in unlocked and key < n:
            # Unlock that box
            unlocked.add(key)
            # Add the keys inside the newly unlocked box to our list of keys
            keys.extend(boxes[key])

    # If we unlocked all boxes, return True; otherwise, return False
    return len(unlocked) == n
