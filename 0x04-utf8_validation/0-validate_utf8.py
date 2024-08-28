#!/usr/bin/python3
"""
Module containing function which validates UTF8 stream
"""
from typing import List


def validUTF8(data):
    important_bytes = []

    for index, number in enumerate(data):
        binary_mask = 0b10000000
        one_count = 0
        if len(bin(number)[2:]) > 8:
            number = int(bin(number)[-8:])

        while binary_mask != 0:
            binary_mask &= number
            binary_mask >>= 1
            if binary_mask != 0:
                one_count += 1

        if 1 < one_count <= 4:
            if len(important_bytes) > 0:
                if index in range(
                    important_bytes[-1][0],
                    important_bytes[-1][1] + 1):
                    return False
            important_bytes.append((index, index + one_count - 1))
            if len(data[index:]) < important_bytes[-1][1] - important_bytes[-1][0] + 1:
                return False
        else:
            if one_count > 4:
                return False
            elif one_count == 1:
                if len(important_bytes) > 0:
                    if index not in range(
                        important_bytes[-1][0],
                        important_bytes[-1][1] + 1):
                        return False
            elif one_count == 0:
                if len(important_bytes) > 0:
                    if index in range(
                          important_bytes[-1][0],
                          important_bytes[-1][0] + 1):
                        return False
    return True
