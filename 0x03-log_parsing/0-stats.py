#!/usr/bin/python3
"""
Module which prints all the status code frequencies and file size
"""
import re
import sys
import signal


line_no = 1
file_size = 0
status_dict = {}

def int_handler(dict_status, size):
    print("File size: {}".format(size))
    for key in sorted(dict_status.keys()):
        print("{}: {}".format(key, dict_status[key]))

for curr_line in sys.stdin:
    regexP = re.compile(r'(\d{1,3}\.){3}\d{1,3}\s\-\s\[.*\]\s\"[A-Z]{1,7}\s/.*/[0-9]{1,4}\sHTTP/\d\.\d\"\s(\d{3})\s(\d{1,4})')
    match = regexP.match(curr_line)

    if match:
        line_file_size = int(match.group(3))
        file_size += line_file_size
        line_code = match.group(2)
        if line_code in status_dict.keys():
            status_dict[line_code] += 1
        else:
            status_dict[line_code] = 1
        # signal.signal(signal.SIGINT, int_handler(status_dict, file_size))

    if (line_no % 10 == 0):
        # print("line No: {}".format(line_no))
        print("File size: {}".format(file_size))
        for key in sorted(status_dict.keys()):
            print("{}: {}".format(key, status_dict[key]))
    line_no += 1
    signal.signal(signal.SIGINT, lambda signum, frame: int_handler(status_dict, file_size))
