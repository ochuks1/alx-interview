#!/usr/bin/python3
"""
Log Parsing Script
Reads input from stdin and computes metrics: total file size and counts of status codes.
"""
import sys

# Initialize variables
total_file_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """
    Print accumulated metrics: total file size and status code counts
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Check if the log line is in the expected format
        if len(parts) >= 7:
            file_size = parts[-1]
            status_code = parts[-2]

            # Update total file size
            try:
                total_file_size += int(file_size)
            except ValueError:
                continue

            # Update status code count
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print final stats upon keyboard interruption
    print_stats()
    sys.exit()

# Print final stats at the end
print_stats()
