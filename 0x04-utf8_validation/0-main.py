#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8
ans_validUTF8 = __import__('0-ans_validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

data = [235, 140]
print(validUTF8(data))
print('*'* 50)
print(ans_validUTF8(data))

data =  [250, 145, 145, 145, 145]
print(validUTF8(data))
print('*'* 50)
print(ans_validUTF8(data))

data =  [345, 467]
print(validUTF8(data))
print('*'* 50)
print(ans_validUTF8(data))
