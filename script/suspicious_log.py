import re
from datetime import datetime as dt
from datetime import timedelta
from collections import deque,defaultdict

def suspicious_log(file):
    pattern = re.compile(r'^(\S*)\s-\s-\s\[(\d{2}\/[a-zA-Z]{2,4}\/\d{4}(:\d{2}){3})\]\s"(POST\s\/login\sHTTP\/1\.[12])"\s(401)\s(\d*)')
    queue = deque()
    map = defaultdict(deque)
    result_map = defaultdict()
    result = []
    if file:
        for line in file:
            match = pattern.search(line)
            if match:
                print(match.groups())
                time_epoch = dt.strptime(match.group(2),"%d/%b/%Y:%H:%M:%S")
                ip = match.group(1)
                # print(time_epoch)
                curr_queue = map[ip]
                curr_queue.append(time_epoch)
                while(curr_queue[-1]-curr_queue[0] > timedelta(seconds=30)):
                    curr_queue.popleft()
                if (len(curr_queue) >= 5):
                    last_alert = result_map.get(ip)
                    if ((last_alert is None) or (time_epoch - last_alert >= timedelta(seconds=30))):
                        result_map[ip] = time_epoch
                        result.append((ip,match.group(2),len(curr_queue)))
                
        print("\n\n")
    return result


def main():
    file_path = "/Users/aryansingh/Documents/bash/script/logs/access.log"
    try:
        with open(file=file_path, mode="r", encoding="latin-1") as f:
            # Assume suspicious_log returns a list of tuples or is a generator
            alerts = suspicious_log(f)
            for ip, ts, count in alerts:
                print(f"ALERT: {ip} flagged at {ts} ({count} attempts in 30s)")

    except FileNotFoundError:
        print("Log file not found.")
        
if __name__ == "__main__":
    main()
