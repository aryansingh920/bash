import datetime
from collections import deque, defaultdict,Counter
import re
import math
# piweba3y.prodigy.com - - [02/Jul/1995:22:23:25 - 0400] "GET /shuttle/countdown/countdown.html HTTP/1.0" 200 3985

def check_rate_limit( log_line,count:Counter,queue:deque, limit=100, window_seconds=60):
    """
    Processes a single log line and returns the IP if it exceeds the limit 
    within the sliding window.
    """
    pattern = r'^(\S+)\s-\s-\s\[(\d{2}/[a-zA-Z]{3}/\d{4}:\d{2}:\d{2}:\d{2})\s-\d{4}\]'
    
    match = re.search(pattern, log_line)

    # If a line is malformed or empty, just skip it—don't crash the architect's system
    if not match:
        return None
    
    try:
        # print("line : ",log_line)
        # print(count,queue,limit,window_seconds)
        ip = match.group(1)
        timestamp = match.group(2)
        time_epoch = datetime.datetime.strptime(timestamp,"%d/%b/%Y:%H:%M:%S")
        queue.append((time_epoch,ip))
        count[time_epoch] = ip
        first_element = queue[0][0]
        last_element = queue[-1][-1]
        first_element_second = first_element.time().second
        last_element_second = last_element.time().second
        
        while (math.abs(last_element_second - first_element_second) < 60):
            # queue.popleft()
            pass
        pass

    except Exception as e:
        # Handle malformed lines gracefully
        print("Error : ",e)
        return None

    return None


def main():
    limit = 5
    log_file_path = "/Users/aryansingh/Documents/bash/script/logs/NASA_access.log"

    # Initialize state outside the loop
    counts = Counter()
    queue = deque()

    print(f"--- Analyzing Logs (Limit: {limit} req/min) ---")

    try:
        # FIX: Use 'latin-1' encoding to prevent UnicodeDecodeError
        with open(log_file_path, 'r', encoding='latin-1') as f:
            for line in f:
                offender = check_rate_limit(line, counts, queue, limit=limit)
                if offender:
                    print(f"ALERT: IP {offender} exceeded {limit} requests!")
    except FileNotFoundError:
        print("Log file not found.")
if __name__ == "__main__":
    main()
