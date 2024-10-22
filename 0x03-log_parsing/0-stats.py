#!/usr/bin/python3
import sys

def main():
    total_file_size = 0
    status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 7:
                continue  # Skip lines that do not match the expected format

            # Extract file size and status code
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
            except ValueError:
                continue  # Skip lines with invalid file size or status code

            # Update the total file size
            total_file_size += file_size

            # Update status code count
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats(total_file_size, status_codes_count)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_codes_count)
        sys.exit()

def print_stats(total_file_size, status_codes_count):
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

if __name__ == "__main__":
    main()
