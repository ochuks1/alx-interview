#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    This code writes a method that determines if all the boxes can be opened. Given that You have n number of locked boxes in front of you. 
    Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
    """

    n = len(boxes)  # Total number of boxes
    opened = [False] * n  # A list to track which boxes are opened
    opened[0] = True  # The first box is unlocked

    # Stack to simulate DFS (starting from box 0)
    stack = [0]

    # Perform DFS to unlock boxes
    while stack:
        current_box = stack.pop()

        # Get the keys inside the current box
        for key in boxes[current_box]:
            if key < n and not opened[key]:  # If the key opens a valid unopened box
                opened[key] = True  # Mark the box as opened
                stack.append(key)  # Add the box to the stack for further exploration

    # Return True if all boxes are opened, False otherwise
    return all(opened)


# Example usage
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], []]  # All boxes can be unlocked
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 2], [0, 3], [4], [], []]  # Some boxes can't be unlocked
    print(canUnlockAll(boxes2))  # Output: False
