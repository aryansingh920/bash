import random
from datetime import datetime, timedelta

ips = [f"192.168.1.{i}" for i in range(100, 110)]
endpoints = ["/index", "/login", "/dashboard", "/api/v1/resource"]
methods = ["GET", "POST"]
statuses = [200, 404, 401, 302]

start_time = datetime(2026, 3, 16, 13, 0, 0)
log_entries = []

for i in range(100000):
    ip = random.choice(ips)
    # Target an IP for a burst attack
    if 900 < i < 950:
        ip = "192.168.1.105"
        method, endpoint, status = "POST", "/login", 401
    else:
        method = random.choice(methods)
        endpoint = random.choice(endpoints)
        status = random.choice(statuses)
    
    # Increment time by random seconds (0-3) to simulate flow
    start_time += timedelta(seconds=random.randint(0, 3))
    ts = start_time.strftime("%d/%b/%Y:%H:%M:%S")
    
    log = f'{ip} - - [{ts}] "{method} {endpoint} HTTP/1.1" {status} {random.randint(100, 2000)}'
    log_entries.append(log)

with open("access.log", "w") as f:
    f.write("\n".join(log_entries))
