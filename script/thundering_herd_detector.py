import json
import os
from collections import defaultdict,deque
import re
from datetime import datetime as dt
from datetime import timedelta

config = {
    "number_of_failed_devices" : 3,
    "time_window" : 60,
}


def rate_limiting(file,config):
    # Keeping your logic placeholder as requested
    
    result = defaultdict(list)
    unique_device = defaultdict(int)
    window_queue = deque() # timestamp, device
    
    pattern = re.compile(
        r'^timestamp="(?P<timestamp>\S+)"\s' +
        r'event="(?P<event>\S+)"\s' +
        r'device_id="(?P<device_id>\S+)"\s' +
        r'status="(?P<status>\S+)"\s' +
        r'[a-zA-Z_]+="(?P<ts>[^"]+)"'
    )
    for line in file:
        # print("Inside the loop")
        match = pattern.search(line)
        # print(match.groupdict())
        if match:
            timestamp = dt.strptime(match.group("timestamp"),"%Y-%m-%dT%H:%M:%SZ")
            if (match.group("status") == "ERROR" and match.group("ts") == "503"):
                device = match.group("device_id")
                
                window_queue.append((timestamp,device))
                unique_device[device] += 1
                
                while (window_queue and timestamp - window_queue[0][0] > timedelta(seconds=config["time_window"])):
                    _,old_device = window_queue.popleft()
                    unique_device[old_device] -= 1
                    if unique_device[old_device] == 0:
                        del unique_device[old_device]
                        
                if len(unique_device) >= config["number_of_failed_devices"]:
                    result[timestamp.isoformat()] = list(unique_device.keys())
                
                
                
            
            # print(match.group("timestamp"))
            

    
    
    return result


if __name__ == "__main__":
    # 1. Path Management
    
    log_dir = os.path.join(os.getcwd(), "script", "logs")
    file_path = os.path.join(log_dir, "apple_device_mgmt.log")

    print(f"\n{' Apple Device Management Analysis':^60}")
    print(f"{'-'*60}")
    print(f"Target: {file_path}")
    print(f"{'-'*60}\n")

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Log file missing: {file_path}")

        with open(file_path, "r") as f:
            result_dict = rate_limiting(f,config)

            # 2. Architect-Style Printing
            if result_dict:
                print(
                    f"✅ ANALYSIS SUCCESSFUL: {len(result_dict)} Windows Flagged\n")

                # Header for the results
                print(f"{'TIMESTAMP':<25} | {'AFFECTED DEVICES'}")
                print(f"{'-'*60}")

                for timestamp, devices in result_dict.items():
                    # Joining device IDs for a clean string
                    device_str = ", ".join(devices)
                    print(f"{timestamp:<25} | {device_str}")
            else:
                print("ℹ️  Scan Complete: No anomalies or rate limits exceeded.")

    except FileNotFoundError as fnf:
        print(f"❌ IO_ERROR: {fnf}")
    except Exception as e:
        print(f"⚠️  SYSTEM_ANOMALY: {type(e).__name__} - {e}")

    print(f"\n{'-'*60}")
    print(f"{'END OF REPORT':^60}\n")
