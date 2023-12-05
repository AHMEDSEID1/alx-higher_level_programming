#!/usr/bin/python3
import sys

def print_metrics(file_size, status_codes):
    print("File size: {}".format(file_size))
    sorted_status_codes = sorted(status_codes.keys())
    for code in sorted_status_codes:
        count = status_codes[code]
        print("{}: {}".format(code, count))

def parse_line(line):
    parts = line.split(" ")
    if len(parts) >= 7:
        file_size = int(parts[-1])
        status_code = parts[-2]
        return file_size, status_code
    return None, None

lines_processed = 0
file_size = 0
status_codes = {}

try:
    for line in sys.stdin:
        file_size_line, status_code_line = parse_line(line)
        if file_size_line is not None and status_code_line is not None:
            file_size += file_size_line
            if status_code_line in status_codes:
                status_codes[status_code_line] += 1
            else:
                status_codes[status_code_line] = 1
        
        lines_processed += 1
        if lines_processed % 10 == 0:
            print_metrics(file_size, status_codes)

except KeyboardInterrupt:
    print_metrics(file_size, status_codes)
