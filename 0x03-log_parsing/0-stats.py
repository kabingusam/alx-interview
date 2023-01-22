import sys
from signal import signal, SIGINT

# Initialize variables to keep track of metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Function to handle keyboard interrupt (CTRL + C)
def handle_interrupt(signal_received, frame):
    print_metrics()
    sys.exit(0)

# Function to print metrics
def print_metrics():
    print("Total file size:", total_size)
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(code, ":", status_codes[code])

# Register the interrupt handler
signal(SIGINT, handle_interrupt)

# Loop through stdin line by line
for line in sys.stdin:
    # Attempt to extract metrics from input line
    try:
        ip, date, request, code, size = line.strip().split()
        code = int(code)
        size = int(size)
    except ValueError:
        # If input line is not in the correct format, skip it
        continue

    # Update metrics
    total_size += size
    if code in status_codes:
        status_codes[code] += 1
    line_count += 1

    # Print metrics every 10 lines or on keyboard interrupt
    if line_count % 10 == 0:
        print_metrics()

# Print metrics one final time after input stream is exhausted
print_metrics()