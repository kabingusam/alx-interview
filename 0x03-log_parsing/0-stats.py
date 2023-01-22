import sys
import re
from collections import defaultdict

pattern = re.compile(r'(\S+) - \[(.+?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')

# initialize metrics to 0
total_hits = 0
total_size = 0
status_codes = defaultdict(int)

try:
    for line in sys.stdin:
        match = pattern.search(line)
        if match:
            # increment metrics
            total_hits += 1
            total_size += int(match.group(4))
            status_codes[match.group(3)] += 1
        else:
            # skip line if it doesn't match the expected format
            continue

        if total_hits % 10 == 0:
            # print out metrics
            print("File size:", total_size)
            for status_code in sorted(status_codes):
                if status_code.isdigit():
                    print("{}: {}".format(status_code, status_codes[status_code]))
            print()
except KeyboardInterrupt:
        # print out metrics
        print("File size:", total_size)
        for status_code in sorted(status_codes):
            if status_code.isdigit():
                print("{}: {}".format(status_code, status_codes[status_code]))
