#!/usr/bin/env python3
import re
import sys
import signal
# import io


line_no = 0
file_size = 0
while sys.stdin.readline():
    curr_line = sys.stdin.readline()
    # regexP = r'(\d{1-3}\.){3}\d{1-3}\s\-\s\[.*\]\s\"[A-Z]{1-7}\s/.*/[0-9]{1-4}\s HTTP/\d\.\d\"\s\d{3}\s\d{1-4}'
    # regexP = re.compile(r'^(\d{1-3}\.){3}\d{1-3}\s\-\s\[.*\]\s\"[A-Z]{1-7}\s/.*/[0-9]{1-4}\s HTTP/\d\.\d\"\s(\d{3})\s(\d{1-4})$')

    regexP = re.compile(r'\d{3}')
    # regexP = re.compile(r'^(\d{1-3}\.){3}\d{1-3}.*$')
    # pattern = regexP.search(curr_line)
    pattern = regexP.findall(curr_line)
    match = regexP.match(curr_line)

    # if match:
    #     print(match.group(0))

    if pattern:
        print(pattern[0:-1])
    # print(curr_line)

    # if match:
    #     print("{}".format(line_no))
    #     line_file_size = int(match.group(3))
    #     print(line_file_size)
    #     file_size += line_file_size
    #     line_code = match.group(2)
    #     print(line_code)
    # else:
    #     line_no += 1
    #     continue
    # line_no += 1
