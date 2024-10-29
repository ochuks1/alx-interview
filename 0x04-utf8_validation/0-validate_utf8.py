#!/usr/bin/python3
"""
This module contains a method that checks if a list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes to check for the current character
    num_bytes = 0

    # Masks to check the most significant bits of a byte
    mask_1_byte = 1 << 7  # 10000000
    mask_2_byte = (1 << 7) + (1 << 6)  # 11000000

    for byte in data:
        # Get the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count the number of 1's to determine the number of bytes
            if (byte >> 5) == 0b110:  # 2-byte
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # Invalid 1-byte character (if first bit is 1)
                return False
        else:
            # We are checking continuation bytes
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If num_bytes is 0, all characters were properly validated
    return num_bytes == 0
