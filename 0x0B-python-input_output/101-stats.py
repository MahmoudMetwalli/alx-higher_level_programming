#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys

# Initialize variables
total_size = 0
status_codes = {}
line_count = 0

try:
    # Loop through each line of stdin
    for line in sys.stdin:
        # Split the line by spaces
        tokens = line.split()
        # Get the file size from the last token
        file_size = int(tokens[-1])
        # Add it to the total size
        total_size += file_size
        # Get the status code from the second last token
        status_code = tokens[-2]
        # Increment the count for that status code
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
        # Increment the line count
        line_count += 1
        # If the line count is a multiple of 10, print the statistics
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            # Sort the status codes by ascending order
            sorted_codes = sorted(status_codes.keys())
            # Print the number of lines for each status code
            for code in sorted_codes:
                print("{}: {}".format(code, status_codes[code]))
except KeyboardInterrupt:
    # If the user presses CTRL + C, print the statistics and exit
    print("File size: {}".format(total_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        print("{}: {}".format(code, status_codes[code]))
    sys.exit(0)
