#!/usr/bin/python3
"""
0-validate_utf8.py
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    byte_count = 0
    for byte in data:
        if byte < 0 or byte > 255:
            return False
        if byte_count == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                byte_count = 1
            elif byte >> 4 == 0b1110:
                byte_count = 2
            elif byte >> 3 == 0b11110:
                byte_byte_count = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                count -= 1
            else:
                return False
    return byte_count == 0
