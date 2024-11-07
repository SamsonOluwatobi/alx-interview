#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 code points."""
    skip = 0
    
    for byte in data:
        if skip > 0:
            # Check continuation byte (should be 10xxxxxx)
            if byte & 0b11000000 != 0b10000000:
                return False
            skip -= 1
        else:
            # Determine the number of bytes in the UTF-8 character
            if byte & 0b10000000 == 0:       # 1-byte (ASCII)
                skip = 0
            elif byte & 0b11100000 == 0b11000000:  # 2-byte sequence
                skip = 1
            elif byte & 0b11110000 == 0b11100000:  # 3-byte sequence
                skip = 2
            elif byte & 0b11111000 == 0b11110000:  # 4-byte sequence
                skip = 3
            else:
                return False  # Invalid first byte
    
    return skip == 0
